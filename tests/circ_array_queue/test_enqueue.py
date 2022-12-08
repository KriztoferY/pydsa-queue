import pytest

from pydsa.queue import CircArrayQueue


class TestEnqueue:
    def test_not_full(self):
        q = CircArrayQueue[int](4, 'int')
        assert q.enqueue(3) is None
        assert len(q) == 1
        q.enqueue(1)
        assert len(q) == 2

    def test_full_and_grow(self):
        q = CircArrayQueue[int](4, 'int')
        q.enqueue(3)
        q.enqueue(1)
        q.enqueue(4)
        q.enqueue(1)
        assert len(q) == 4
        assert q._capacity == 4
        q.enqueue(5)
        assert q._capacity == 8
        q.enqueue(9)
        assert len(q) == 6
        assert q._capacity == 8
