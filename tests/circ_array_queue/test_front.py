import pytest

from pydsa.queue import CircArrayQueue


class TestFront:
    def test_empty(self):
        q = CircArrayQueue[int](4, 'int')
        with pytest.raises(RuntimeError):
            q.front()

    def test_size_gt_1(self):
        q = CircArrayQueue[int](4, 'int')
        q.enqueue(3)
        q.enqueue(1)
        q.enqueue(4)
        assert len(q) == 3
        assert q.front() == 3
        assert len(q) == 3

    def test_size_eq_1(self):
        q = CircArrayQueue[int](4, 'int')
        q.enqueue(3)
        assert len(q) == 1
        assert q.front() == 3
        assert len(q) == 1
