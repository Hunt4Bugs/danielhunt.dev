"""Engine tests. Everything runs against the synthetic fixture, never against docs/."""

from __future__ import annotations

import re
import shutil

import pytest

from dh import types
from dh.cli import main
from dh.doc import Document
from dh.errors import EXIT_INVALID, EXIT_OK
from dh.lint import ERROR, Linter
from dh.model import Model, parse_values_table, split_row


# -- documents: round-trip ---------------------------------------------------------


@pytest.mark.parametrize(
    "relative",
    [
        "docs/_protocol/concepts/concept.md",
        "docs/_protocol/taxonomies/status.md",
        "docs/example/concepts/gadget.md",
        "docs/example/gadgets/alpha.md",
        "docs/example/domain.md",
    ],
)
def test_render_is_idempotent(example_repo, relative):
    """Rendering canonicalizes, and rendering a canonical file changes nothing.

    Byte-identity with hand-authored input is deliberately *not* asserted: YAML has several
    spellings for one value (a folded `>-` block and a plain scalar carry the same string), so
    the first write normalizes. What must hold — and what makes two agents writing the same
    values produce the same bytes — is that the canonical form is a fixed point.
    """
    path = example_repo / relative
    document = Document.parse(path.read_text(), path=str(path))
    keys, sections = list(document.front_matter), list(document.sections)
    once = document.render(key_order=keys, section_order=sections)
    twice = Document.parse(once).render(key_order=keys, section_order=sections)
    assert once == twice


@pytest.mark.parametrize(
    "relative",
    ["docs/example/gadgets/alpha.md", "docs/example/domain.md", "docs/example/README.md"],
)
def test_canonical_files_round_trip_exactly(example_repo, relative):
    """A file already in canonical form is reproduced byte for byte."""
    path = example_repo / relative
    original = path.read_text()
    document = Document.parse(original, path=str(path))
    keys, sections = list(document.front_matter), list(document.sections)
    assert document.render(key_order=keys, section_order=sections) == original


def test_parse_preserves_values_across_canonicalization(example_repo):
    """Canonicalizing changes the spelling, never the value."""
    path = example_repo / "docs/_protocol/concepts/concept.md"
    before = Document.parse(path.read_text(), path=str(path))
    after = Document.parse(before.render(key_order=list(before.front_matter)))
    assert after.front_matter == before.front_matter
    assert after.sections == before.sections


def test_body_parser_ignores_headings_inside_code_fences():
    text = "---\nid: x\n---\n\n# T\n\n## Real\n\n```\n## Not a heading\n```\n"
    document = Document.parse(text)
    assert list(document.sections) == ["Real"]
    assert "## Not a heading" in document.sections["Real"]


def test_write_is_deterministic(example_repo):
    path = example_repo / "docs/example/gadgets/alpha.md"
    document = Document.read(str(path))
    keys, sections = list(document.front_matter), list(document.sections)
    first = document.render(key_order=keys, section_order=sections)
    second = Document.parse(first).render(key_order=keys, section_order=sections)
    assert first == second


# -- slugs and ids -----------------------------------------------------------------


@pytest.mark.parametrize(
    "value,expected",
    [
        ("Competitor", "competitor"),
        ("Hook → Journey → Payoff", "hook-journey-payoff"),
        ("Novel / Unusual Visual", "novel-unusual-visual"),
        ("Scroll Stopper + Verbal Hook → Development → Payoff",
         "scroll-stopper-verbal-hook-development-payoff"),
        ("Myth vs Fact", "myth-vs-fact"),
        ("  Leading and trailing  ", "leading-and-trailing"),
    ],
)
def test_slug(value, expected):
    assert types.slug(value) == expected


def test_forbidden_terms_name_their_replacement():
    """Every excluded OWL term explains what to use instead, so the error is actionable."""
    assert "owl:minCardinality" in types.FORBIDDEN_TERMS
    assert "rdfs:domain" in types.FORBIDDEN_TERMS
    for term, why in types.FORBIDDEN_TERMS.items():
        assert why and isinstance(why, str), term


# -- taxonomy tables ---------------------------------------------------------------


def test_split_row_honours_escaped_pipe():
    assert split_row(r"| a \| b | c |") == ["a | b", "c"]


def test_values_table_maps_columns_by_header():
    raw = "| Value | Stable code | Meaning |\n| --- | --- | --- |\n| Fine | F | Works. |"
    values, problems = parse_values_table(raw)
    assert not problems
    assert values[0]["skos:prefLabel"] == "Fine"
    assert values[0]["skos:notation"] == "F"
    assert values[0]["skos:definition"] == "Works."


def test_unmapped_column_is_reported_not_dropped():
    raw = "| Value | Wingspan |\n| --- | --- |\n| Fine | 3m |"
    _values, problems = parse_values_table(raw)
    assert any("Wingspan" in problem for problem in problems)


def test_values_table_reports_slug_collision():
    raw = "| Value |\n| --- |\n| A / B |\n| A - B |"
    _values, problems = parse_values_table(raw)
    assert any("slug" in problem for problem in problems)


# -- contracts ---------------------------------------------------------------------


def test_contract_reads_both_storage_locations(example_repo):
    model = Model.load(str(example_repo))
    instance = model.instance("example.gadget.alpha")
    fields = model.contract_for(instance).read_all(instance.document)
    assert fields["name"] == "alpha gadget"          # front matter
    assert fields["grade"] == "Fine"                 # front matter, controlled
    assert fields["tags"] == ["one", "two"]          # body, list
    assert fields["summary"].startswith("A synthetic")  # body, prose


def test_declaration_order_is_serialization_order(example_repo):
    model = Model.load(str(example_repo))
    contract = model.concept("example.gadget").contract
    assert contract.section_order() == ["Tags", "Summary"]
    order = contract.key_order()
    assert order.index("name") < order.index("grade") < order.index("related")


def test_derived_property_may_not_carry_constraints(example_repo):
    model = Model.load(str(example_repo))
    concept = model.concept("example.gadget")
    spec = concept.contract.properties[0]
    spec.raw["derived"] = {"owl:inverseOf": "example.gadget.name"}
    spec.derived = spec.raw["derived"]
    assert any("no sh: constraints" in problem for problem in spec.structural_errors())


# -- lint --------------------------------------------------------------------------


def test_fixture_is_clean(example_repo):
    findings = Linter(Model.load(str(example_repo))).run()
    assert [f.as_text() for f in findings if f.severity == ERROR] == []


def _first_error(repo, check=None):
    findings = Linter(Model.load(str(repo))).run()
    errors = [f for f in findings if f.severity == ERROR]
    if check:
        errors = [f for f in errors if f.check == check]
    return errors


def test_lint_catches_unresolved_body_link(example_repo):
    """The check that would have caught the retired registry paths in the topic template."""
    path = example_repo / "docs/example/gadgets/alpha.md"
    path.write_text(path.read_text() + "\nSee [gone](../nowhere/missing.md).\n")
    assert _first_error(example_repo, "links")


def test_lint_ignores_links_inside_code_spans(example_repo):
    path = example_repo / "docs/example/gadgets/alpha.md"
    path.write_text(path.read_text() + "\nWrite it as `- [Label](path.md)`.\n")
    assert not _first_error(example_repo, "links")


def test_lint_catches_unknown_taxonomy_value(example_repo):
    path = example_repo / "docs/example/gadgets/alpha.md"
    path.write_text(path.read_text().replace("grade: Fine", "grade: Sublime"))
    errors = _first_error(example_repo, "taxonomy-values")
    assert errors and "Sublime" in errors[0].message


def test_lint_catches_undeclared_body_section(example_repo):
    """This is what replaces the unmanaged_sections escape hatch."""
    path = example_repo / "docs/example/gadgets/alpha.md"
    path.write_text(path.read_text() + "\n## Surprise\n\nUndeclared.\n")
    assert _first_error(example_repo, "body-sections")


def test_lint_catches_undeclared_frontmatter_key(example_repo):
    path = example_repo / "docs/example/gadgets/alpha.md"
    path.write_text(path.read_text().replace("name: alpha gadget", "name: alpha gadget\ncolour: red"))
    errors = _first_error(example_repo, "closed")
    assert errors and "colour" in errors[0].message


def test_lint_catches_id_not_derived_from_type(example_repo):
    path = example_repo / "docs/example/gadgets/alpha.md"
    path.write_text(path.read_text().replace("id: example.gadget.alpha", "id: example.widget.alpha"))
    assert _first_error(example_repo, "ids")


def test_lint_catches_bad_status(example_repo):
    path = example_repo / "docs/example/gadgets/alpha.md"
    path.write_text(path.read_text().replace("status: active", "status: reference"))
    errors = _first_error(example_repo, "status")
    assert errors and "reference" in errors[0].message


def test_lint_catches_foreign_file_in_instance_directory(example_repo):
    (example_repo / "docs/example/gadgets/stray.md").write_text(
        "---\nid: example.note.stray\nrdf:type: protocol.note\ndomain: example\n"
        "status: active\nversion: 1\n---\n\n# Stray\n"
    )
    assert _first_error(example_repo, "structure")


def test_missing_required_value_is_error_only_when_active(example_repo):
    """Severity is scoped by status: a draft is already an honest label for incompleteness."""
    path = example_repo / "docs/example/gadgets/alpha.md"
    without_summary = re.sub(r"## Summary.*", "", path.read_text(), flags=re.S)
    path.write_text(without_summary)
    assert _first_error(example_repo, "cardinality")

    path.write_text(without_summary.replace("status: active", "status: draft"))
    assert not _first_error(example_repo, "cardinality")


def test_draft_record_produces_no_sources_finding(example_repo):
    path = example_repo / "docs/example/gadgets/alpha.md"
    path.write_text(path.read_text().replace("status: active", "status: draft"))
    findings = Linter(Model.load(str(example_repo))).run()
    assert not [
        f for f in findings if f.check == "sources" and f.file.endswith("alpha.md")
    ]


# -- the two claims the whole design rests on --------------------------------------


def test_new_domain_needs_no_engine_code(example_repo, tmp_path):
    """A domain the engine has never heard of loads, queries and lints — files only.

    Nothing under src/dh/ is touched. If adding a domain required an engine change, this is the
    test that would fail.
    """
    source = example_repo / "docs/example"
    target = example_repo / "docs/widget"
    shutil.copytree(source, target)

    def retype(path, *pairs):
        text = path.read_text()
        for old, new in pairs:
            text = text.replace(old, new)
        path.write_text(text)

    for path in target.rglob("*.md"):
        retype(path, ("example", "widget"), ("Example", "Widget"), ("Gadget", "Doohickey"),
               ("gadget", "doohickey"))
    (target / "concepts" / "gadget.md").rename(target / "concepts" / "doohickey.md")
    (target / "taxonomies" / "gadget-grade.md").rename(
        target / "taxonomies" / "doohickey-grade.md"
    )
    (target / "gadgets").rename(target / "doohickeys")

    model = Model.load(str(example_repo))
    assert "widget" in model.domains
    assert "widget.doohickey" in model.concepts
    assert len(model.instances_of("widget.doohickey")) == 2
    assert model.taxonomy("Doohickey Grade").labels
    assert [f for f in Linter(model).run() if f.severity == ERROR] == []


def test_engine_names_no_domain(repo_root):
    """No module under src/dh/ mentions any live domain or concept name.

    Self-updating: the names are read from the repository at test time, so adding a domain
    automatically extends what this guards.
    """
    model = Model.load(str(repo_root))
    banned = set(model.domains) | {
        types.concept_slug(cid) for cid in model.concepts
    }
    # Structural names the protocol itself defines are not domain names.
    banned -= {"protocol", "concept", "domain", "taxonomy", "workflow", "router", "note", "skill"}
    assert banned, "expected some domain names to guard"

    offenders = []
    for path in (repo_root / "src" / "dh").rglob("*.py"):
        if "migrate" in path.parts:  # one-off sweeps are allowed to name what they migrate
            continue
        text = path.read_text()
        for name in banned:
            if re.search(rf"\b{re.escape(name)}\b", text):
                offenders.append(f"{path.name}: {name}")
    assert not offenders, f"engine names a domain: {offenders}"


# -- CLI ---------------------------------------------------------------------------


def test_cli_lint_exit_codes(example_repo, capsys):
    assert main(["--root", str(example_repo), "lint"]) == EXIT_OK
    path = example_repo / "docs/example/gadgets/alpha.md"
    path.write_text(path.read_text().replace("grade: Fine", "grade: Sublime"))
    assert main(["--root", str(example_repo), "lint"]) == EXIT_INVALID


def test_cli_taxonomy_check_refuses_unapproved_value(example_repo):
    """A governed refusal is distinguishable from a lint failure by its exit code."""
    assert main(["--root", str(example_repo), "taxonomy", "check", "Gadget Grade", "Fine"]) == 0
    assert main(["--root", str(example_repo), "taxonomy", "check", "Gadget Grade", "Sublime"]) != 0


def test_cli_get_reads_a_concept_and_an_instance(example_repo, capsys):
    assert main(["--root", str(example_repo), "get", "example.gadget"]) == EXIT_OK
    assert "owl:Class" in capsys.readouterr().out
    assert main(["--root", str(example_repo), "get", "example.gadget.alpha"]) == EXIT_OK
    assert "alpha gadget" in capsys.readouterr().out


def test_cli_list_filters_by_field(example_repo, capsys):
    main(["--root", str(example_repo), "--text", "list", "example.gadget", "--where", "grade=Fine"])
    assert "example.gadget.alpha" in capsys.readouterr().out
    main(["--root", str(example_repo), "--text", "list", "example.gadget", "--where", "grade=Poor"])
    assert "example.gadget.alpha" not in capsys.readouterr().out


def test_cli_unknown_instance_exits_not_found(example_repo):
    assert main(["--root", str(example_repo), "get", "example.gadget.nope"]) == 3


# -- validation gaps reported on PR #40 --------------------------------------------
# Each of these three passed lint before the fix, letting an invalid record through the
# conformance gate. They are regression tests, not hypotheticals.


def test_single_valued_property_reports_extra_values(example_repo):
    """A two-value list in a maxCount:1 property must fail, not be silently truncated.

    read() projects a single-valued property to a scalar, so counting the projection would
    report 1 and hide the violation. The count must come from what the file authored.
    """
    path = example_repo / "docs/example/gadgets/alpha.md"
    path.write_text(path.read_text().replace("grade: Fine", "grade:\n  - Fine\n  - Poor"))
    errors = _first_error(example_repo, "cardinality")
    assert errors and "at most 1, found 2" in errors[0].message


def test_read_authored_preserves_what_the_file_wrote(example_repo):
    """The projection stays lossy on purpose; the authored values stay available beside it."""
    path = example_repo / "docs/example/gadgets/alpha.md"
    path.write_text(path.read_text().replace("grade: Fine", "grade:\n  - Fine\n  - Poor"))
    model = Model.load(str(example_repo))
    instance = model.instance("example.gadget.alpha")
    spec = model.contract_for(instance).get("grade")
    assert spec.read(instance.document) == "Fine"
    assert spec.read_authored(instance.document) == ["Fine", "Poor"]


def test_missing_scheme_is_reported_for_a_controlled_property(example_repo):
    """A controlled property whose scheme does not exist would otherwise accept any value.

    The membership check silently has nothing to check against, so the absent scheme has to be
    caught where it is declared.
    """
    concept = example_repo / "docs/example/concepts/gadget.md"
    concept.write_text(
        concept.read_text().replace(
            "skos:inScheme: example.taxonomy.gadget-grade",
            "skos:inScheme: example.taxonomy.does-not-exist",
        )
    )
    instance = example_repo / "docs/example/gadgets/alpha.md"
    instance.write_text(instance.read_text().replace("grade: Fine", "grade: CompletelyMadeUp"))
    errors = _first_error(example_repo, "ranges")
    assert errors and "does-not-exist" in errors[0].message


def _add_maker_property(example_repo, value):
    """Give Gadget a reference property ranging over Gadget, and point it at `value`."""
    concept = example_repo / "docs/example/concepts/gadget.md"
    concept.write_text(
        concept.read_text().replace(
            "  - id: tags",
            "  - id: maker\n"
            "    rdf:type: owl:ObjectProperty\n"
            "    rdfs:label: Maker\n"
            "    rdfs:range: example.gadget\n"
            "    sh:maxCount: 1\n"
            "    store: frontmatter\n"
            "  - id: tags",
        )
    )
    instance = example_repo / "docs/example/gadgets/alpha.md"
    instance.write_text(instance.read_text().replace("grade: Fine", f"grade: Fine\nmaker: {value}"))


def test_reference_to_the_wrong_concept_is_an_error(example_repo):
    """Existence is not type-checking: the target must be an instance of the declared range."""
    _add_maker_property(example_repo, "../taxonomies/gadget-grade.md")
    errors = _first_error(example_repo, "ranges")
    assert errors and "is a `protocol.taxonomy`" in errors[0].message


def test_reference_to_the_right_concept_passes(example_repo):
    """The type check must not reject a correct reference."""
    _add_maker_property(example_repo, "beta.md")
    assert not _first_error(example_repo, "ranges")


def test_reference_to_an_untyped_file_is_distinguished_from_a_missing_one(example_repo):
    """A not-yet-conformed target is a different finding from a dangling one."""
    (example_repo / "docs/example/loose.md").write_text("no front matter here\n")
    _add_maker_property(example_repo, "../loose.md")
    findings = Linter(Model.load(str(example_repo))).run()
    messages = [f.message for f in findings if f.check == "ranges"]
    assert any("not a typed record" in m for m in messages), messages
    assert not any("does not resolve" in m for m in messages), messages
