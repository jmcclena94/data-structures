# coding=utf-8
import pytest


PUSH_TABLE = [
    ([50, 30, 20, 25, 27, 22, 45], [50, 30, 45, 25, 27, 20, 22]),
    ([1, 2, 3, 4, 5, 6, 7], [7, 4, 6, 1, 3, 2, 5])
]

POP_TABLE = [
    ([10, 20, 25, 50, 3, 16], [25, 16, 20, 10, 3]),
    ([1, 2, 3, 4, 5, 6, 7], [6, 4, 5, 1, 3, 2])
]


@pytest.mark.parametrize('value, result', PUSH_TABLE)
def test_push(value, result):
    from binheap import Binheap
    new_heap = Binheap()
    new_heap.push(value)
    assert new_heap.binheap == result


@pytest.mark.parametrize('value, result', POP_TABLE)
def test_pop(value, result):
    from binheap import Binheap
    new_heap = Binheap()
    new_heap.push(value)
    new_heap.pop()
    assert new_heap.binheap == result
