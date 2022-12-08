import pytest

from pydsa.queue import CircArrayQueue


class TestDequeue:
    def test_empty(self):
        q = CircArrayQueue[int](4, 'int')
        with pytest.raises(RuntimeError):
            q.dequeue()

    def test_size_gt_1(self):
        q = CircArrayQueue[int](4, 'int')
        q.enqueue(3)
        q.enqueue(1)
        q.enqueue(4)
        assert len(q) == 3
        assert q.dequeue() == 3
        assert q.front() == 1
        assert len(q) == 2

    def test_size_eq_1(self):
        q = CircArrayQueue[int](4, 'int')
        q.enqueue(3)
        assert len(q) == 1
        q.dequeue()
        assert len(q) == 0

    def test_shrink(self):
        q = CircArrayQueue[int](8, 'int')
        q.enqueue(3)
        q.enqueue(1)
        q.enqueue(4)
        q.enqueue(1)
        q.enqueue(5)
        q.enqueue(9)
        q.enqueue(2)
        assert len(q) == 7
        assert q._capacity == 8
        assert q.dequeue() == 3
        assert q.dequeue() == 1
        assert q.dequeue() == 4
        assert q.dequeue() == 1
        assert q.dequeue() == 5
        assert q._capacity == 8
        assert q.dequeue() == 9
        assert len(q) == 1
        assert q._capacity == 4
        assert q.front() == 2
