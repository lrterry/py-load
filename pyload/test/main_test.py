from pyload.__main__ import load_config
import pytest

required_config = [
    'url',
    'endpoints'
]


def test_load_config_throws_error():
    with pytest.raises(FileNotFoundError):
        load_config('')


def test_loads_config():
    config = load_config('./test/test.yml')
    assert config is not None


def test_config_required_fields():
    config = load_config('./test/test.yml')
    for field in required_config:
        assert field in config
