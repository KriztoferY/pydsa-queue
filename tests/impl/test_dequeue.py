import pytest

from pydsa.queue import CircArrayQueue
from pydsa.queue import SLListQueue


@pytest.fixture(params=[CircArrayQueue, SLListQueue])
def queue(request):
    if request.param is CircArrayQueue:
        return request.param[int](8, 'int')
    elif request.param is SLListQueue:
        return request.param[int]('int')
    else:
        raise RuntimeError("unsupported queue type")


class TestDequeue:
    def test_empty(self, queue):
        with pytest.raises(RuntimeError):
            queue.dequeue()

    def test_size_gt_1(self, queue):
        queue.enqueue(3)
        queue.enqueue(1)
        queue.enqueue(4)
        assert len(queue) == 3
        assert queue.dequeue() == 3
        assert queue.front() == 1
        assert len(queue) == 2

    def test_size_eq_1(self, queue):
        queue = CircArrayQueue[int](4, 'int')
        queue.enqueue(3)
        assert len(queue) == 1
        queue.dequeue()
        assert len(queue) == 0

    def test_shrink(self, queue):
        queue = CircArrayQueue[int](8, 'int')
        queue.enqueue(3)
        queue.enqueue(1)
        queue.enqueue(4)
        queue.enqueue(1)
        queue.enqueue(5)
        queue.enqueue(9)
        queue.enqueue(2)
        assert len(queue) == 7
        assert queue._capacity == 8
        assert queue.dequeue() == 3
        assert queue.dequeue() == 1
        assert queue.dequeue() == 4
        assert queue.dequeue() == 1
        assert queue.dequeue() == 5
        assert queue._capacity == 8
        assert queue.dequeue() == 9
        assert len(queue) == 1
        assert queue._capacity == 4
        assert queue.front() == 2
