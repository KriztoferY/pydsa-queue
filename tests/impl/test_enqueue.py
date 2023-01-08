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


class TestEnqueue:
    def test_not_full(self, queue):
        assert queue.enqueue(3) is None
        assert len(queue) == 1
        queue.enqueue(1)
        assert len(queue) == 2

    def test_full_and_grow(self, queue):
        if type(queue) is CircArrayQueue:
            queue.enqueue(3)
            queue.enqueue(1)
            queue.enqueue(4)
            queue.enqueue(1)
            assert len(queue) == 4
            assert queue._capacity == 4
            queue.enqueue(5)
            assert queue._capacity == 8
            queue.enqueue(9)
            assert len(queue) == 6
            assert queue._capacity == 8
