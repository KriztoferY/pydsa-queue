import pytest

from pydsa.queue import CircArrayQueue


class TestLenAndEmpty:
    def test_len_new(self):
        q = CircArrayQueue[int](8, 'int')
        assert len(q) == 0
        assert q.empty

    def test_len_nonempty(self):
        q = CircArrayQueue[int](8, 'int')
        q.enqueue(3)
        q.enqueue(1)
        q.enqueue(4)
        assert len(q) == 3
        assert not q.empty
