import pytest
from pyload.load import BaseLoadTester


@pytest.fixture(scope='module')
def base():
    base = BaseLoadTester('test')
    yield base


class TestBaseLoadTester(object):

    def test_init(self, base):
        assert base.config == 'test'

    def test_before(self, base):
        with pytest.raises(NotImplementedError):
            base.before()

    def test_on_result(self, base):
        with pytest.raises(NotImplementedError):
            base.on_result()
