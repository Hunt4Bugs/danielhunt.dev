"""Reading the model: projecting instances, filtering, searching, and expanding references."""

from __future__ import annotations

import re

from .errors import UsageError
from .lint import LINK_RE

WHERE_RE = re.compile(r"^([A-Za-z_][\w:.-]*)\s*(=|!=|~)\s*(.*)$")


def project(model, instance):
    """Flatten an instance to {id, path, rdf:type, fields{}} using its contract."""
    contract = model.contract_for(instance)
    document = instance.document
    fields = contract.read_all(document) if contract else {}
    return {
        "id": instance.id,
        "rdf:type": instance.concept_id,
        "domain": instance.domain_id,
        "status": document.front_matter.get("status"),
        "path": model.rel(document.path),
        "fields": fields,
    }


def project_concept(model, concept):
    return {
        "id": concept.id,
        "rdf:type": "owl:Class",
        "domain": concept.domain_id,
        "label": concept.label,
        "path": model.rel(concept.document.path),
        "persistence": concept.persistence,
        "title_field": concept.title_field,
        "properties": [
            {
                "id": spec.id,
                "rdf:type": spec.rdf_type,
                "rdfs:range": spec.range,
                "skos:inScheme": spec.in_scheme,
                "sh:minCount": spec.min_count,
                "sh:maxCount": spec.max_count,
                "store": spec.store,
                "section": spec.section,
                "format": spec.format,
                "derived": spec.derived,
            }
            for spec in concept.contract.properties
        ],
    }


def parse_where(clauses):
    parsed = []
    for clause in clauses or []:
        match = WHERE_RE.match(clause)
        if not match:
            raise UsageError(
                f"cannot parse --where '{clause}'", hint="expected field=value, field!=value"
            )
        parsed.append((match.group(1), match.group(2), match.group(3)))
    return parsed


def matches(record, conditions):
    for field, operator, wanted in conditions:
        actual = record["fields"].get(field, record.get(field))
        values = actual if isinstance(actual, list) else ([] if actual is None else [actual])
        values = [str(v) for v in values]
        if operator == "=":
            if wanted == "null":
                if values:
                    return False
            elif wanted not in values:
                return False
        elif operator == "!=":
            if wanted in values:
                return False
        elif operator == "~":
            if not any(wanted.lower() in value.lower() for value in values):
                return False
    return True


def search(model, record, terms):
    """Token scan over every readable value. Narrows candidates; it does not judge duplication."""
    if not terms:
        return True
    blob = " ".join(str(v) for v in _flatten(record["fields"])).lower()
    instance = model.instances.get(record["id"])
    if instance:
        blob += " " + " ".join(instance.document.sections.values()).lower()
        if instance.document.h1:
            blob += " " + instance.document.h1.lower()
    return all(term.lower() in blob for term in terms)


def _flatten(fields):
    for value in fields.values():
        if isinstance(value, list):
            for item in value:
                yield item
        elif value is not None:
            yield value


def expand(model, record, paths):
    """Follow dotted reference paths, deduplicating targets — the graph join, done once."""
    for dotted in paths or []:
        segments = dotted.split(".")
        current = [record]
        for segment in segments:
            nxt = []
            seen = set()
            for item in current:
                for target in _resolve(model, item, segment):
                    if target["id"] in seen:
                        continue
                    seen.add(target["id"])
                    nxt.append(target)
            current = nxt
        record.setdefault("expanded", {})[dotted] = current
    return record


def _resolve(model, record, field):
    values = record.get("fields", {}).get(field)
    values = values if isinstance(values, list) else ([] if values is None else [values])
    out = []
    for value in values:
        target = _lookup(model, record, value)
        if target:
            out.append(target)
    return out


def _lookup(model, record, value):
    if not value:
        return None
    text = str(value)
    if text in model.instances:
        return project(model, model.instances[text])
    match = LINK_RE.search(text)
    target = match.group(1) if match else text
    import os

    source = model.instances.get(record["id"])
    if not source:
        return None
    resolved = os.path.normpath(
        os.path.join(os.path.dirname(source.document.path), target.split("#", 1)[0])
    )
    for instance in model.instances.values():
        if os.path.abspath(instance.document.path) == os.path.abspath(resolved):
            return project(model, instance)
    return None
