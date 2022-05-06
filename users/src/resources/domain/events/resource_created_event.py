from importlib.resources import Resource

from shared.domain.events.event import Event


class ResourceCreatedEvent(Event):
    EVENT_NAME = "resource_created"

    def __init__(self, id, name, status):
        super().__init__(event_name=ResourceCreatedEvent.EVENT_NAME, aggregate_id=id)
        self.id = id
        self.name = name
        self.status = status

    def toProperties(self):
        return dict(
            id=self.id,
            name=self.name,
            status=self.status
        )
