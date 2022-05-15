from ..data_structures.singleton import Singleton
from .container import Container
from users.infrastructure.dependency_injection.users_module import set_users_module
from characters.infrastructure.dependency_injection.characters_module import set_characters_module
from comics.infrastructure.dependency_injection.comics_module import set_comics_module


class App(object, metaclass=Singleton):
    def __init__(self):
        self.container = Container()
        self.container.init_resources()
        self.container.wire(modules=[__name__])

    def set_users_module(self):
        set_users_module(self.container)

    def set_characters_module(self):
        set_characters_module(self.container)

    def set_comics_module(self):
        set_comics_module(self.container)
