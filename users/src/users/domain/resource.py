from shared.domain.aggregate_root import AggregateRoot
from resources.domain.events.resource_created_event import ResourceCreatedEvent


class Resource(AggregateRoot):
    def __init__(self, id, name, status='status'):
        super().__init__()
        self.__id = id
        self.__name = name
        self.__status = status

    def toProperties(self):
        return dict(
            id=self.__id,
            name=self.__name,
            status=self.__status
        )

    def handleCreation(self):
        event = ResourceCreatedEvent(
            id=self.__id,
            name=self.__name,
            status=self.__status
        )

        self.record(event=event)
