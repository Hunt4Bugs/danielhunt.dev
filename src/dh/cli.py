"""The `dh` command line. One JSON envelope, one exit-code contract."""

from __future__ import annotations

import argparse
import json
import os
import sys

from . import query, types
from .errors import DhError, NotFound, UsageError
from .errors import EXIT_INTERNAL, EXIT_INVALID, EXIT_OK
from .lint import ADVISORY, ERROR, WARN, Linter, counts
from .model import Model

PROTOCOL_VERSION = "1.0"


def envelope(command, data=None, diagnostics=None, meta=None, ok=True):
    return {
        "ok": ok,
        "command": command,
        "protocol": PROTOCOL_VERSION,
        "data": data if data is not None else {},
        "diagnostics": diagnostics or [],
        "meta": meta or {},
    }


def emit(payload, as_text=False, text_lines=None):
    if as_text and text_lines is not None:
        for line in text_lines:
            print(line)
    else:
        print(json.dumps(payload, indent=2, ensure_ascii=False, default=str))


# -- commands -------------------------------------------------------------------


def cmd_domains(model, args):
    rows = []
    for domain in sorted(model.domains.values(), key=lambda d: d.id):
        concepts = [c for c in model.concepts.values() if c.domain_id == domain.id]
        rows.append(
            {
                "id": domain.id,
                "label": domain.label,
                "root": model.rel(domain.root),
                "concepts": len(concepts),
                "iri": types.domain_iri(model.base_iri, domain.id),
            }
        )
    lines = [f"{r['id']:<12} {r['root']:<20} {r['concepts']:>3} concepts" for r in rows]
    return envelope("domains", rows, meta={"count": len(rows)}), lines


def cmd_concepts(model, args):
    rows = []
    for concept in sorted(model.concepts.values(), key=lambda c: c.id):
        if args.domain and concept.domain_id != args.domain:
            continue
        rows.append(
            {
                "id": concept.id,
                "label": concept.label,
                "domain": concept.domain_id,
                "persisted": concept.mode == "directory",
                "mode": concept.mode,
                "path": model.rel(concept.document.path),
                "properties": len(concept.contract.properties),
            }
        )
    lines = [f"{r['id']:<28} {str(r['mode'] or '-'):<10} {r['properties']:>2} props" for r in rows]
    return envelope("concepts", rows, meta={"count": len(rows)}), lines


def cmd_get(model, args):
    identifier = args.identifier
    if identifier in model.concepts:
        data = query.project_concept(model, model.concepts[identifier])
        return envelope("get", data), [json.dumps(data, indent=2, default=str)]
    instance = model.instance(identifier)
    data = query.project(model, instance)
    query.expand(model, data, args.expand)
    return envelope("get", data), [json.dumps(data, indent=2, default=str)]


def cmd_list(model, args):
    concept = model.concept(args.concept)
    conditions = query.parse_where(args.where)
    terms = args.search or []
    rows = []
    for instance in sorted(model.instances_of(concept.id), key=lambda i: i.id):
        record = query.project(model, instance)
        if not query.matches(record, conditions):
            continue
        if not query.search(model, record, terms):
            continue
        query.expand(model, record, args.expand)
        rows.append(record)
    lines = [f"{r['id']:<44} {r['status'] or '-'}" for r in rows]
    return envelope("list", rows, meta={"count": len(rows)}), lines


def cmd_taxonomy(model, args):
    if args.taxonomy_command == "list":
        rows = [
            {
                "name": tax.name,
                "id": tax.id,
                "domain": tax.domain_id,
                "values": len(tax.values),
                "path": model.rel(tax.document.path),
            }
            for tax in sorted(model.taxonomies.values(), key=lambda t: t.name)
        ]
        lines = [f"{r['name']:<32} {r['values']:>3} values  {r['path']}" for r in rows]
        return envelope("taxonomy list", rows, meta={"count": len(rows)}), lines

    tax = model.taxonomy(args.name)
    data = {
        "name": tax.name,
        "id": tax.id,
        "owner": model.rel(tax.document.path),
        "values": tax.values,
    }
    if args.taxonomy_command == "values":
        lines = [row["skos:prefLabel"] for row in tax.values]
        return envelope("taxonomy values", data), lines

    # check
    wanted = args.value
    allowed = set(tax.labels)
    if wanted in allowed:
        return envelope("taxonomy check", {"name": tax.name, "value": wanted, "known": True}), [
            f"ok: '{wanted}' is in {tax.name}"
        ]
    raise DhError(
        f"'{wanted}' is not a value of {tax.name}",
        hint=(
            f"owner: {model.rel(tax.document.path)}. Propose it through govern-taxonomy; "
            "never write an unapproved value."
        ),
    )


def load_baseline(path):
    """Read the suppression set: findings already known and being burned down."""
    if not path or not os.path.exists(path):
        return set()
    with open(path, encoding="utf-8") as handle:
        entries = json.load(handle).get("suppressed", [])
    return {(entry.get("file"), entry.get("check"), entry.get("message")) for entry in entries}


def cmd_lint(model, args):
    linter = Linter(model)
    findings = linter.run(args.paths)

    if args.write_baseline:
        payload = {
            "note": (
                "Findings already known when a wave landed. This file shrinks every wave and is "
                "deleted when the conformance sweep completes. It is a burndown, not an ignore "
                "list: nothing is added to it without a wave that will remove it."
            ),
            "suppressed": [
                {"file": f.file, "check": f.check, "message": f.message}
                for f in findings
                if f.severity == ERROR
            ],
        }
        with open(args.write_baseline, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, ensure_ascii=False)
            handle.write("\n")

    baseline = load_baseline(args.baseline)
    if baseline:
        findings = [
            f for f in findings if (f.file, f.check, f.message) not in baseline
        ]

    tally = counts(findings)
    failing = tally[ERROR] > 0 or (args.strict and tally[WARN] > 0)
    payload = envelope(
        "lint",
        {"counts": tally, "findings": [f.as_dict() for f in findings]},
        meta={
            "domains": len(model.domains),
            "concepts": len(model.concepts),
            "taxonomies": len(model.taxonomies),
            "instances": len(model.instances),
        },
        ok=not failing,
    )
    lines = [f.as_text() for f in findings]
    lines.append(
        f"{tally[ERROR]} errors, {tally[WARN]} warnings, {tally[ADVISORY]} advisory "
        f"across {len(model.domains)} domains"
    )
    lines.append(
        "check 'sources' is advisory only: semantic claim-backing is NOT machine-checkable "
        "and remains human review (PROTOCOL.md §17)."
    )
    return payload, lines, (EXIT_INVALID if failing else EXIT_OK)


def cmd_slug(model, args):
    value = types.slug(args.value)
    data = {"input": args.value, "slug": value}
    if args.into:
        concept = model.concept(args.into)
        existing = {types.split_id(i.id)[-1] for i in model.instances_of(concept.id)}
        candidate, counter = value, 2
        while candidate in existing:
            candidate = f"{value}-{counter}"
            counter += 1
        data["slug"] = candidate
        data["collided"] = candidate != value
    return envelope("slug", data), [data["slug"]]


# -- parser ---------------------------------------------------------------------


def build_parser():
    parser = argparse.ArgumentParser(prog="dh", description=__doc__)
    parser.add_argument("--root", help="repository root (default: search upward for docs/)")
    parser.add_argument("--text", action="store_true", help="human-readable output")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("domains", help="list declared domains")

    concepts = sub.add_parser("concepts", help="list concepts")
    concepts.add_argument("--domain")

    get = sub.add_parser("get", help="read one concept or instance")
    get.add_argument("identifier")
    get.add_argument("--expand", action="append", default=[])

    listing = sub.add_parser("list", help="list instances of a concept")
    listing.add_argument("concept")
    listing.add_argument("--where", action="append", default=[])
    listing.add_argument("--search", action="append", default=[])
    listing.add_argument("--expand", action="append", default=[])

    taxonomy = sub.add_parser("taxonomy", help="inspect controlled vocabularies")
    tsub = taxonomy.add_subparsers(dest="taxonomy_command", required=True)
    tsub.add_parser("list")
    values = tsub.add_parser("values")
    values.add_argument("name")
    check = tsub.add_parser("check")
    check.add_argument("name")
    check.add_argument("value")

    lint = sub.add_parser("lint", help="validate the model as written")
    lint.add_argument("paths", nargs="*")
    lint.add_argument("--strict", action="store_true", help="warnings fail too")
    lint.add_argument("--baseline", help="JSON file of findings to suppress while burning down")
    lint.add_argument("--write-baseline", help="record current errors as the baseline")

    slug = sub.add_parser("slug", help="derive a slug")
    slug.add_argument("value")
    slug.add_argument("--into", help="concept id, to suffix on collision")

    return parser


HANDLERS = {
    "domains": cmd_domains,
    "concepts": cmd_concepts,
    "get": cmd_get,
    "list": cmd_list,
    "taxonomy": cmd_taxonomy,
    "lint": cmd_lint,
    "slug": cmd_slug,
}


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        model = Model.load(args.root)
        result = HANDLERS[args.command](model, args)
        if len(result) == 3:
            payload, lines, code = result
        else:
            payload, lines = result
            code = EXIT_OK
        emit(payload, as_text=args.text, text_lines=lines)
        return code
    except DhError as exc:
        payload = envelope(args.command, ok=False)
        payload["error"] = exc.as_dict()
        emit(payload)
        print(f"{exc.code}: {exc.message}", file=sys.stderr)
        if exc.hint:
            print(f"hint: {exc.hint}", file=sys.stderr)
        return exc.exit_code
    except BrokenPipeError:
        return EXIT_OK
    except Exception as exc:  # noqa: BLE001 - surfaced as exit 5 with a traceback on stderr
        import traceback

        traceback.print_exc()
        payload = envelope(getattr(args, "command", "?"), ok=False)
        payload["error"] = {"code": "INTERNAL", "message": str(exc)}
        emit(payload)
        return EXIT_INTERNAL


if __name__ == "__main__":
    raise SystemExit(main())
