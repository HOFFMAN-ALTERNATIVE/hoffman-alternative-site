"""Validate the data files against the minimum schema.

TODO: validate real data files in CI once they exist; check links are https and dates are ISO.
"""
import json
import sys

REQUIRED = {
    "data/projects.example.json": {"title", "summary", "url"},
    "data/releases.example.json": {"title", "type", "date", "links"},
}


def main() -> int:
    bad = 0
    for path, keys in REQUIRED.items():
        for i, row in enumerate(json.load(open(path, encoding="utf-8"))):
            missing = keys - row.keys()
            if missing:
                print(f"{path}[{i}] missing {sorted(missing)}")
                bad = 1
    return bad


if __name__ == "__main__":
    sys.exit(main())
