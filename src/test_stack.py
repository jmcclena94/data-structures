# coding=utf-8
import pytest


PUSH_TABLE = [
    ([1, 2, 3, 4, 5], 5),
    (10, 10)
]

POP_TABLE = [
    ([1, 2, 3, 4, 5], 5),
    (10, 10)
]


@pytest.mark.parametrize('value, result', PUSH_TABLE)
def test_push(value, result):
    from stack import Stack
    assert Stack(value).stack.head.value == result


@pytest.mark.parametrize('value, result', POP_TABLE)
def test_pop(value, result):
    from stack import Stack
    A = Stack(value)
    assert A.pop() == result
