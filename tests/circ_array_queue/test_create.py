import pytest

from pydsa.queue import CircArrayQueue


class TestCreate:
    def test_create_from_positive_init_cap(self):
        assert CircArrayQueue(8)

    def test_create_from_non_pos_init_cap_should_fail(self):
        with pytest.raises(ValueError):
            CircArrayQueue(-1)
