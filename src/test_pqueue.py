# encoding utf-8


import pytest


INSERT_TABLE = [
    ([(1, 100), (2, 99), (3, 98), (4, 97), (5, 96)],
        [(5, 96), (4, 97), (2, 99), (1, 100), (3, 98)])
]

POP_TABLE = [
    ([(1, 100), (2, 99), (3, 98), (4, 97), (5, 96)],
        [96, 97, 98])
]

PEEK_TABLE = [
    ([(1, 100), (2, 99), (3, 98), (4, 97), (5, 96)],
        [(5, 96)])
]


@pytest.mark.parametrize('value, result', INSERT_TABLE)
def test_make_pqueue(value, result):
    """Test insert()."""
    from pqueue import Pqueue
    new_pqueue = Pqueue(value)
    assert new_pqueue.pqueue == result


@pytest.mark.parametrize('value, result', POP_TABLE)
def test_pop_pqueue(value, result):
    """Test pop()."""
    from pqueue import Pqueue
    new_pqueue = Pqueue(value)
    assert new_pqueue.pop() == result[0]
    assert new_pqueue.pop() == result[1]
    assert new_pqueue.pop() == result[2]


@pytest.mark.parametrize('value, result', PEEK_TABLE)
def test_peek_pqueue(value, result):
    """Test peek()."""
    from pqueue import Pqueue
    new_pqueue = Pqueue(value)
    assert new_pqueue.peek() == result[0]
