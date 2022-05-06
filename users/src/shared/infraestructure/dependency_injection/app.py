from ..data_structures.singleton import Singleton
from .container import Container
from users.infraestructure.dependency_injection.users_module import setUsersModule


class App(object, metaclass=Singleton):
    def __init__(self):
        self.container = Container()
        self.container.init_resources()
        self.container.wire(modules=[__name__])

    def setDependencyInjection(self):
        setUsersModule(self.container)
