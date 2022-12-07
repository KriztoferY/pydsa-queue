from collections.abc import Iterable, Sized

import pytest

from pydsa.queue import IQueue


class TestIQueue:
    def test_not_instantiable(self):
        with pytest.raises(TypeError):
            IQueue()

    def test_is_iterable(self):
        assert issubclass(IQueue, Iterable)

    def test_is_sized(self):
        assert issubclass(IQueue, Sized)
