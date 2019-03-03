from pyload.__main__ import load_config
import pytest


def test_load_config_throws_error():
    with pytest.raises(NotImplementedError):
        load_config('')