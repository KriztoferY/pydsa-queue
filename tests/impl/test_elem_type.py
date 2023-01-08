from typing import Type
import pytest

from pydsa.queue import CircArrayQueue
from pydsa.queue import SLListQueue
from pydsa.utils import ElemTypeName


@pytest.fixture(params=[CircArrayQueue, SLListQueue])
def queue(elm_type: Type, type_name: ElemTypeName, request):
    if request.param is CircArrayQueue:
        return request.param[elm_type](8, type_name)
    elif request.param is SLListQueue:
        return request.param[elm_type](type_name)
    else:
        raise RuntimeError("unsupported queue type")


class TestElemType:
    @pytest.mark.parametrize("elm_type, type_name", [
        (int, 'int'),
        (int, 'uint'),
        (float, 'float'),
        (float, 'double'),
        (object, 'object')]
    )
    def test_property(self, elm_type, type_name, queue):
        assert queue.element_type == type_name
