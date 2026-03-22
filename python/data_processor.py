"""Utilities for loading, transforming, and summarizing tabular data."""

import csv
import json
import statistics
from pathlib import Path
from typing import Any


def load_csv(filepath: str) -> list[dict[str, str]]:
    """Load a CSV file and return a list of row dicts."""
    with open(filepath, newline="") as f:
        return list(csv.DictReader(f))


def load_json(filepath: str) -> Any:
    """Load a JSON file."""
    with open(filepath) as f:
        return json.load(f)


def save_json(data: Any, filepath: str, indent: int = 2) -> None:
    """Save data to a JSON file."""
    with open(filepath, "w") as f:
        json.dump(data, f, indent=indent)


def filter_rows(rows: list[dict], key: str, value: str) -> list[dict]:
    """Return rows where row[key] == value."""
    return [r for r in rows if r.get(key) == value]


def pluck(rows: list[dict], key: str) -> list:
    """Extract a single column from a list of row dicts."""
    return [r[key] for r in rows if key in r]


def numeric_summary(values: list[float]) -> dict[str, float]:
    """Return basic descriptive statistics for a list of numbers."""
    if not values:
        return {}
    return {
        "count": len(values),
        "min": min(values),
        "max": max(values),
        "mean": statistics.mean(values),
        "median": statistics.median(values),
        "stdev": statistics.stdev(values) if len(values) > 1 else 0.0,
    }


def group_by(rows: list[dict], key: str) -> dict[str, list[dict]]:
    """Group a list of row dicts by the value of a given key."""
    groups: dict[str, list[dict]] = {}
    for row in rows:
        groups.setdefault(row.get(key, ""), []).append(row)
    return groups


def flatten(nested: list[list]) -> list:
    """Flatten one level of nesting."""
    return [item for sublist in nested for item in sublist]


def deduplicate(rows: list[dict], key: str) -> list[dict]:
    """Remove duplicate rows based on a key field, keeping first occurrence."""
    seen: set = set()
    result = []
    for row in rows:
        val = row.get(key)
        if val not in seen:
            seen.add(val)
            result.append(row)
    return result


if __name__ == "__main__":
    sample = [
        {"name": "Alice", "dept": "Engineering", "salary": "95000"},
        {"name": "Bob", "dept": "Marketing", "salary": "72000"},
        {"name": "Carol", "dept": "Engineering", "salary": "105000"},
        {"name": "Dave", "dept": "Marketing", "salary": "68000"},
        {"name": "Eve", "dept": "Engineering", "salary": "88000"},
    ]

    eng = filter_rows(sample, "dept", "Engineering")
    salaries = [float(r["salary"]) for r in eng]
    print("Engineering salary stats:", numeric_summary(salaries))

    by_dept = group_by(sample, "dept")
    for dept, members in by_dept.items():
        print(f"\n{dept}: {[r['name'] for r in members]}")
