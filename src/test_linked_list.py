# coding=utf-8
import pytest


NODE_TABLE = [
    (5, 5)
]

INSERT_TABLE = [
    (5, 5)
]


POP_TABLE = [
    (7, 7)
]

LENGTH_LIST = [
    (10, 1)
]

SEARCH_LIST = [
    (10, 10)
]

REMOVE_LIST = [
    (6, 5)
]

DISPLAY_LIST = [
    (6, (7, 6))
]


@pytest.mark.parametrize('value, result', NODE_TABLE)
def test_node(value, result):
    from linked_list import Node
    assert Node(value).value == result


@pytest.mark.parametrize('value, result', INSERT_TABLE)
def test_linked_list(value, result):
    from linked_list import LinkedList
    A = LinkedList()
    A.insert(value)
    assert A.head.value == result


@pytest.mark.parametrize('value, result', POP_TABLE)
def test_pop_list(value, result):
    from linked_list import LinkedList
    A = LinkedList()
    A.insert(value)
    assert A.pop() == result


@pytest.mark.parametrize('value, result', LENGTH_LIST)
def test_length_list(value, result):
    from linked_list import LinkedList
    A = LinkedList()
    A.insert(value)
    assert A.size() == result


@pytest.mark.parametrize('value, result', SEARCH_LIST)
def test_search_list(value, result):
    from linked_list import LinkedList
    A = LinkedList()
    A.insert(value)
    assert A.search(value).value == result


@pytest.mark.parametrize('value, result', REMOVE_LIST)
def test_remove_list(value, result):
    from linked_list import LinkedList
    A = LinkedList()
    A.insert(5)
    A.insert(6)
    A.insert(7)
    A.remove(value)
    assert A.head.next_node.value == result


@pytest.mark.parametrize('value, result', DISPLAY_LIST)
def test_display_list(value, result):
    from linked_list import LinkedList
    A = LinkedList()
    A.insert(6)
    A.insert(7)
    assert A.display() == result
