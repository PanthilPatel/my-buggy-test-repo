"""In-memory storage backend for todo items."""

from dataclasses import dataclass, field


@dataclass
class Task:
    id: int
    title: str
    completed: bool = False
    priority: int = 3  # 1 = highest, 5 = lowest


class Storage:
    def __init__(self):
        self._tasks: dict[int, Task] = {}
        self._next_id = 1

    def add(self, title: str, priority: int = 3) -> Task:
        task = Task(id=self._next_id, title=title, priority=priority)
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def get(self, task_id: int) -> Task:
        return self._tasks[task_id]

    def all(self) -> list[Task]:
        return list(self._tasks.values())

    def delete(self, task_id: int) -> None:
        del self._tasks[task_id]
