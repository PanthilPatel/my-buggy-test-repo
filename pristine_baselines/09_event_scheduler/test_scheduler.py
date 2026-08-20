import pytest

from event import Event
from scheduler import events_overlap, find_conflicts, sort_by_start


def test_overlapping_events_detected():
    a = Event("Meeting A", start=60, end=120)
    b = Event("Meeting B", start=90, end=150)
    assert events_overlap(a, b) is True


def test_back_to_back_events_do_not_overlap():
    a = Event("Meeting A", start=60, end=120)
    b = Event("Meeting B", start=120, end=180)  # starts exactly when A ends
    assert events_overlap(a, b) is False


def test_non_overlapping_events():
    a = Event("Meeting A", start=60, end=90)
    b = Event("Meeting B", start=100, end=130)
    assert events_overlap(a, b) is False


def test_find_conflicts_excludes_back_to_back():
    events = [
        Event("A", start=0, end=60),
        Event("B", start=60, end=120),
        Event("C", start=90, end=150),
    ]
    conflicts = find_conflicts(events)
    names = [(a.name, b.name) for a, b in conflicts]
    assert ("A", "B") not in names
    assert ("B", "C") in names


def test_sort_by_start_orders_events():
    events = [
        Event("Late", start=200, end=250),
        Event("Early", start=10, end=50),
        Event("Mid", start=100, end=150),
    ]
    sorted_events = sort_by_start(events)
    assert [e.name for e in sorted_events] == ["Early", "Mid", "Late"]
