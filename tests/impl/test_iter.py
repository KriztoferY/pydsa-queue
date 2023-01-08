import pytest

from pydsa.queue import CircArrayQueue
from pydsa.queue import SLListQueue


nums = (3, 1, 4, 1, 5, 9, 2, 6)


@pytest.fixture(params=[CircArrayQueue, SLListQueue])
def queue(request):
    q = None
    if request.param is CircArrayQueue:
        q = request.param[int](8, 'int')
    elif request.param is SLListQueue:
        q = request.param[int]('int')
    else:
        raise RuntimeError("unsupported queue type")

    for num in nums:
        q.enqueue(num)

    return q


class TestIter:
    def test_iter(self, queue):
        for i, elem in enumerate(queue):
            assert elem == nums[i]
