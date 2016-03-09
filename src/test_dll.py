# coding=utf-8
import pytest


INSERT_TABLE = [
    ([3, 3])
]

APPEND_TABLE = [
    ([10, 10])
]

REMOVE_TABLE = [
    ([21, 20])
]


@pytest.mark.parametrize('value, result', INSERT_TABLE)
def test_insert(value, result):
    from dll import DoubleLink
    A = DoubleLink([])
    A.insert(value)
    assert A.head.value == result


@pytest.mark.parametrize('value, result', APPEND_TABLE)
def test_append(value, result):
    from dll import DoubleLink
    A = DoubleLink([1])
    A.append(value)
    assert A.head.next_node.value == result


def test_pop():
    from dll import DoubleLink
    A = DoubleLink([1, 2, 3])
    result = A.head.value
    assert A.pop() == result


def test_shift():
    from dll import DoubleLink
    A = DoubleLink([1, 2, 3])
    result = A.head.next_node.next_node.value
    assert A.shift() == result


@pytest.mark.parametrize('value, result', REMOVE_TABLE)
def test_remove(value, result):
    from dll import DoubleLink
    A = DoubleLink([18, 19, 20, 21, 22])
    A.remove(value)
    assert A.head.next_node.value == result
