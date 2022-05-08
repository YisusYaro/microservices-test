from shared.domain.aggregate_root import AggregateRoot


class User(AggregateRoot):
    def __init__(self, id, name, image, appearances):
        super().__init__()
        self.__id = id
        self.__name = name
        self.__image = image
        self.__appearances = appearances

    def toProperties(self):
        return dict(
            id=self.__id,
            name=self.__name,
            image=self.__image,
            appearances=self.__appearances,
        )
