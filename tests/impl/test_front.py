import pytest

from pydsa.queue import CircArrayQueue
from pydsa.queue import SLListQueue


@pytest.fixture(params=[CircArrayQueue, SLListQueue])
def queue(request):
    if request.param is CircArrayQueue:
        return request.param[int](4, 'int')
    elif request.param is SLListQueue:
        return request.param[int]('int')
    else:
        raise RuntimeError("unsupported queue type")


class TestFront:
    def test_empty(self, queue):
        with pytest.raises(RuntimeError):
            queue.front()

    def test_size_gt_1(self, queue):
        queue.enqueue(3)
        queue.enqueue(1)
        queue.enqueue(4)
        assert len(queue) == 3
        assert queue.front() == 3
        assert len(queue) == 3

    def test_size_eq_1(self, queue):
        queue.enqueue(3)
        assert len(queue) == 1
        assert queue.front() == 3
        assert len(queue) == 1
