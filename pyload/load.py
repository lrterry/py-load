class BaseLoadTester(object):
    def __init__(self, config):
        self.config = config

    def before(self):
        raise NotImplementedError()

    def on_result(self):
        raise NotImplementedError()
