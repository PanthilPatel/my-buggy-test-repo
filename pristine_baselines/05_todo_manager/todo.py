"""High-level todo list operations built on top of Storage.

Contains two bugs:
1. `pending_tasks` uses an inverted condition and returns completed
   tasks instead of pending ones.
2. `sort_by_priority` sorts in descending order, but priority 1 is
   supposed to be "highest" and should come first (ascending order).
"""

from storage import Storage, Task


class TodoManager:
    def __init__(self):
        self.storage = Storage()

    def add_task(self, title: str, priority: int = 3) -> Task:
        return self.storage.add(title, priority)

    def complete(self, task_id: int) -> None:
        task = self.storage.get(task_id)
        task.completed = True

    def pending_tasks(self) -> list[Task]:
        # BUG: condition is inverted -- this returns tasks that ARE
        # completed, not the pending ones.
        return [t for t in self.storage.all() if t.completed]

    def completed_tasks(self) -> list[Task]:
        return [t for t in self.storage.all() if t.completed]

    def sort_by_priority(self) -> list[Task]:
        # BUG: reverse=True sorts highest number first, but priority
        # 1 is supposed to be the highest priority and should appear
        # first, so this should sort ascending (reverse=False).
        return sorted(self.storage.all(), key=lambda t: t.priority, reverse=True)
