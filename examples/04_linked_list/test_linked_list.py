import pytest

from linked_list import LinkedList


def test_to_list_roundtrip():
    ll = LinkedList().from_list([1, 2, 3, 4])
    assert ll.to_list() == [1, 2, 3, 4]


def test_reverse_preserves_all_nodes():
    ll = LinkedList().from_list([1, 2, 3, 4])
    ll.reverse()
    assert ll.to_list() == [4, 3, 2, 1]


def test_reverse_two_elements():
    ll = LinkedList().from_list([1, 2])
    ll.reverse()
    assert ll.to_list() == [2, 1]


def test_reverse_single_element():
    ll = LinkedList().from_list([42])
    ll.reverse()
    assert ll.to_list() == [42]


def test_reverse_empty_list():
    ll = LinkedList()
    ll.reverse()
    assert ll.to_list() == []
