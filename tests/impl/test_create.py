import pytest

from pydsa.queue import CircArrayQueue
from pydsa.queue import SLListQueue


@pytest.mark.parametrize("queue_type", [CircArrayQueue, SLListQueue])
class TestCreate:
    def test_create_from_positive_init_cap(self, queue_type):
        if queue_type is CircArrayQueue:
            assert queue_type[int](8, 'int') is not None
        elif queue_type is SLListQueue:
            assert queue_type[int]('int') is not None
        else:
            raise TypeError("unsupported queue_type")

    def test_create_from_non_pos_init_cap_should_fail(self, queue_type):
        if queue_type is CircArrayQueue:
            with pytest.raises(ValueError):
                queue_type[int](-1, 'int')
            with pytest.raises(ValueError):
                queue_type[int](0, 'int')
        elif queue_type is SLListQueue:
            pass
        else:
            raise TypeError("unsupported queue_type")
