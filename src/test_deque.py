# coding=utf-8
import pytest


APPEND_TABLE = [
    (10, 10)
]

APPEND_LEFT_TABLE = [
    (20, 20)
]

POP_TABLE = [
    (5, 5)
]

POP_LEFT_TABLE = [
    (7, 7)
]

PEEK_TABLE = [
    (7, 7)
]

PEEK_LEFT_TABLE = [
    (70, 70)
]


@pytest.mark.parametrize('value, result', APPEND_TABLE)
def test_append(value, result):
    from deque import Deque
    new_deque = Deque()
    new_deque.append(value)
    assert new_deque.container.head.value == result


@pytest.mark.parametrize('value, result', APPEND_LEFT_TABLE)
def test_append_left(value, result):
    from deque import Deque
    new_deque = Deque()
    new_deque.appendleft(value)
    assert new_deque.container.head.value == result


@pytest.mark.parametrize('value, result', POP_TABLE)
def test_pop(value, result):
    from deque import Deque
    new_deque = Deque()
    new_deque.appendleft(value)
    assert new_deque.pop() == result


def test_pop_error():
    from deque import Deque
    with pytest.raises(AttributeError):
        new_deque = Deque()
        new_deque.pop()


@pytest.mark.parametrize('value, result', POP_LEFT_TABLE)
def test_pop_left(value, result):
    from deque import Deque
    new_deque = Deque()
    new_deque.append(value)
    assert new_deque.popleft() == result


def test_pop_left_error():
    from deque import Deque
    with pytest.raises(AttributeError):
        new_deque = Deque()
        new_deque.popleft()


@pytest.mark.parametrize('value, result', PEEK_TABLE)
def test_peek(value, result):
    from deque import Deque
    new_deque = Deque()
    new_deque.append(10)
    new_deque.append(value)
    assert new_deque.peek() == result


@pytest.mark.parametrize('value, result', PEEK_LEFT_TABLE)
def test_peek_left(value, result):
    from deque import Deque
    new_deque = Deque()
    new_deque.append(value)
    new_deque.append(10)
    assert new_deque.peekleft() == result


def test_size():
    from deque import Deque
    new_deque = Deque()
    new_deque.append(10)
    new_deque.append(20)
    new_deque.append(30)
    new_deque.append(40)
    new_deque.pop()
    new_deque.popleft()
    assert new_deque.length == 2
