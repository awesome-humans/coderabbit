"""Write a copy of a JSON Schema that rejects unknown keys in every object.

CodeRabbit's schema closes only a few of its objects, so a misspelt key such as
`reviews.profil` validates, and CodeRabbit then ignores it without an error.
Every object that lists its properties and sets no `additionalProperties` of
its own gets `additionalProperties: false`.

Usage: python strict_schema.py <schema.json> <out.json>
"""

import json
import sys


def close(node: object) -> None:
    if isinstance(node, dict):
        if "properties" in node and "additionalProperties" not in node:
            node["additionalProperties"] = False
        for value in node.values():
            close(value)
    elif isinstance(node, list):
        for value in node:
            close(value)


def main() -> None:
    source, target = sys.argv[1], sys.argv[2]
    with open(source, encoding="utf-8") as f:
        schema = json.load(f)
    close(schema)
    with open(target, "w", encoding="utf-8") as f:
        json.dump(schema, f)


if __name__ == "__main__":
    main()
