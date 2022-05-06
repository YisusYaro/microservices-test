from ..data_structures.singleton import Singleton
from .container import Container


class App(object, metaclass=Singleton):
    def __init__(self):
        self.container = Container()
        self.container.init_resources()
        self.container.wire(modules=[__name__])
