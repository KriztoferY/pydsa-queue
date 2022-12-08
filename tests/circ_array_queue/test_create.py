import pytest

from pydsa.queue import CircArrayQueue


class TestCreate:
    def test_create_from_positive_init_cap(self):
        assert CircArrayQueue[int](8, 'int') is not None

    def test_create_from_non_pos_init_cap_should_fail(self):
        with pytest.raises(ValueError):
            CircArrayQueue[int](-1, 'int')
        with pytest.raises(ValueError):
            CircArrayQueue[int](0, 'int')
