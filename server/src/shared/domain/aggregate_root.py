from shared.infrastructure.dependency_injection import app


class AggregateRoot(object):
    def __init__(self):
        self.__events = []
        self.__eventBus = app.App().container.EventBus()

    def record(self, event):
        self.__events.append(event)

    def commit(self):
        for event in self.__events:
            self.__eventBus.execute(event)
