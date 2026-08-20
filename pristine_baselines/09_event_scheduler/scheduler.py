"""Simple event scheduler that detects overlapping events.

Contains a bug: `events_overlap` uses `<=`/`>=` comparisons, so two
events that merely touch at a shared boundary (one ends exactly when
the other starts) are incorrectly flagged as overlapping.
"""

from event import Event


def events_overlap(a: Event, b: Event) -> bool:
    # BUG: back-to-back events (a.end == b.start) should NOT count as
    # overlapping, but `<=`/`>=` treats a shared boundary as overlap.
    return a.start <= b.end and b.start <= a.end


def find_conflicts(events: list[Event]) -> list[tuple[Event, Event]]:
    conflicts = []
    for i in range(len(events)):
        for j in range(i + 1, len(events)):
            if events_overlap(events[i], events[j]):
                conflicts.append((events[i], events[j]))
    return conflicts


def sort_by_start(events: list[Event]) -> list[Event]:
    return sorted(events, key=lambda e: e.start)
