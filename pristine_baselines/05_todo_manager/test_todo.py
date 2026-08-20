import pytest

from todo import TodoManager


def build_manager():
    m = TodoManager()
    m.add_task("Buy milk", priority=3)
    m.add_task("File taxes", priority=1)
    m.add_task("Water plants", priority=5)
    return m


def test_pending_tasks_excludes_completed():
    m = build_manager()
    all_ids = [t.id for t in m.storage.all()]
    m.complete(all_ids[0])
    pending = m.pending_tasks()
    assert all(not t.completed for t in pending)
    assert len(pending) == 2


def test_completed_tasks_only_completed():
    m = build_manager()
    all_ids = [t.id for t in m.storage.all()]
    m.complete(all_ids[1])
    completed = m.completed_tasks()
    assert len(completed) == 1
    assert completed[0].id == all_ids[1]


def test_sort_by_priority_highest_first():
    m = build_manager()
    sorted_tasks = m.sort_by_priority()
    priorities = [t.priority for t in sorted_tasks]
    # priority 1 = highest priority, should be first
    assert priorities == [1, 3, 5]


def test_add_task_returns_task_with_title():
    m = TodoManager()
    task = m.add_task("Read a book")
    assert task.title == "Read a book"
    assert task.completed is False
