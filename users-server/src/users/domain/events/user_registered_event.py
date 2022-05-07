from shared.domain.events.event import Event


class UserRegisteredEvent(Event):
    EVENT_NAME = "user_registered"

    def __init__(self, id, name):
        super().__init__(event_name=UserRegisteredEvent.EVENT_NAME, aggregate_id=id)
        self.id = id
        self.name = name

    def toProperties(self):
        return dict(
            id=self.id,
            name=self.name,
        )
