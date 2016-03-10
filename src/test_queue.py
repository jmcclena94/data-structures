# coding=utf-8
import pytest


ENQUEUE_TABLE = [
    ([1, 2, 3], 3)
]

DEQUEUE_TABLE = [
    ([1, 2, 3], 1)
]

PEEK_TABLE = [
    ([1, 2, 3], 1),
    ([], None)
]

SIZE_TABLE = [
    ([1, 2, 3], 3),
    ([], 0)
]


@pytest.mark.parametrize('value, result', ENQUEUE_TABLE)
def test_enqueue(value, result):
    from queue import Queue
    test_queue = Queue()
    test_queue.enqueue(value)
    assert test_queue.head.value == result


@pytest.mark.parametrize('value, result', DEQUEUE_TABLE)
def test_dequeue(value, result):
    from queue import Queue
    test_queue = Queue()
    test_queue.enqueue(value)
    assert test_queue.dequeue() == result


def test_dequeue_error():
    from queue import Queue
    test_queue = Queue()
    with pytest.raises(ValueError):
        test_queue.dequeue()


@pytest.mark.parametrize('value, result', PEEK_TABLE)
def test_peek(value, result):
    from queue import Queue
    test_queue = Queue()
    test_queue.enqueue(value)
    assert test_queue.peek() == result


@pytest.mark.parametrize('value, result', SIZE_TABLE)
def test_size(value, result):
    from queue import Queue
    test_queue = Queue()
    test_queue.enqueue(value)
    assert test_queue.length == result
