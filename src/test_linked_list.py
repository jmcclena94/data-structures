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
