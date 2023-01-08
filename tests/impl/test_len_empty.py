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


class TestLenAndEmpty:
    def test_len_new(self, queue):
        assert len(queue) == 0
        assert queue.empty

    def test_len_nonempty(self, queue):
        queue.enqueue(3)
        queue.enqueue(1)
        queue.enqueue(4)
        assert len(queue) == 3
        assert not queue.empty
