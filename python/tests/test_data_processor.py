"""Tests for data_processor.py"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from data_processor import (
    filter_rows, pluck, numeric_summary,
    group_by, flatten, deduplicate,
)

ROWS = [
    {"id": "1", "dept": "Eng", "score": "90"},
    {"id": "2", "dept": "HR", "score": "75"},
    {"id": "3", "dept": "Eng", "score": "85"},
    {"id": "4", "dept": "HR", "score": "80"},
    {"id": "1", "dept": "Eng", "score": "90"},  # duplicate
]


def test_filter_rows():
    result = filter_rows(ROWS, "dept", "Eng")
    assert len(result) == 3
    assert all(r["dept"] == "Eng" for r in result)


def test_pluck():
    assert pluck(ROWS, "dept") == ["Eng", "HR", "Eng", "HR", "Eng"]


def test_numeric_summary():
    stats = numeric_summary([10, 20, 30, 40, 50])
    assert stats["count"] == 5
    assert stats["min"] == 10
    assert stats["max"] == 50
    assert stats["mean"] == 30
    assert stats["median"] == 30


def test_numeric_summary_empty():
    assert numeric_summary([]) == {}


def test_group_by():
    groups = group_by(ROWS, "dept")
    assert set(groups.keys()) == {"Eng", "HR"}
    assert len(groups["Eng"]) == 3
    assert len(groups["HR"]) == 2


def test_flatten():
    assert flatten([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]
    assert flatten([]) == []


def test_deduplicate():
    unique = deduplicate(ROWS, "id")
    ids = pluck(unique, "id")
    assert ids == ["1", "2", "3", "4"]
