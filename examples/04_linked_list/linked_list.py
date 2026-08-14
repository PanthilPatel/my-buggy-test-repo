"""Singly linked list implementation.

Contains a bug: `reverse` loses track of the tail pointer during
iteration, so the resulting list is missing its last original node
(the traversal terminates one step early).
"""

from __future__ import annotations


class Node:
    def __init__(self, value, next: "Node | None" = None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    def from_list(self, values: list) -> "LinkedList":
        for v in values:
            self.append(v)
        return self

    def append(self, value) -> None:
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node

    def to_list(self) -> list:
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

    def reverse(self) -> None:
        prev = None
        current = self.head
        # BUG: the loop condition checks `current.next` instead of
        # `current`, so it stops one node early and the original
        # tail node is dropped from the reversed list.
        while current is not None and current.next is not None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev
