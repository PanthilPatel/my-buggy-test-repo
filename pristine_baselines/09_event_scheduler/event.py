"""Event data model for the scheduler."""

from dataclasses import dataclass


@dataclass
class Event:
    name: str
    start: int  # minutes since midnight
    end: int    # minutes since midnight

    def __post_init__(self):
        if self.end <= self.start:
            raise ValueError("Event end must be after start")
