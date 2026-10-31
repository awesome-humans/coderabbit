# Review instructions

These instructions tune automated pull request review in this repository. The agent reviewer (currently CodeRabbit) reads them, and so can any other agent asked to review a pull request here.

This repository holds `.coderabbit.yaml`, the central CodeRabbit configuration that every awesome-humans repository without its own file uses. CodeRabbit ignores an unknown key or a bad value silently, so a finding matters when it would change every repository's reviews without an error.

## What Important means here

Reserve Important for these. Everything else is Nit at most.

- **A key that does nothing.** A key or value that CodeRabbit's schema doesn't define at that level, or one it has deprecated. The `config` job catches unknown keys, so report what it can't: a value of the right type that the schema's description says does something else.
- **A blocking review.** `request_changes_workflow` set to `true`, which lets CodeRabbit block merges. Its reviews stay advisory.
- **Text leaking into history.** `high_level_summary` set to `true` without `high_level_summary_in_walkthrough`, or any `high_level_summary_placeholder`. Either puts a summary in the pull request description, and so in the squash commit.
- **A guideline dropped.** A `knowledge_base.code_guidelines.filePatterns` list that no longer includes `**/AGENTS.md`, `**/REVIEW.md`, or `website:pages/conventions/*.md`.
- **A path filter that hides content.** A `path_filters` entry that excludes `opinions/`, `templates/`, `skills/`, or a root Markdown file.
- **A weakened validator.** A change to `scripts/strict_schema.py` or `validate.yml` that lets an unknown key through.
- **A loosened review.** A change to this file that drops an Important item, raises the nit cap, or skips a class of finding, without saying why. The agent reviewer can read it from the pull request itself, so the change would soften its own review.

## Cap the nits

Report at most three Nits per review. Writing-style findings, from [awesome-humans/website: Writing style](https://github.com/awesome-humans/website/blob/main/pages/conventions/writing-style.md), are Nit at most.

## Do not report

- Anything the `config` job already checks: unknown keys and values of the wrong type.
- An issue the pull request didn't introduce or make worse.

## Evidence

Cite `file:line`, and quote the schema's description for any finding about what a key does.
