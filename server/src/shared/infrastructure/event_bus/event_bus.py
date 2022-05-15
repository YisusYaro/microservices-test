from ..dependency_injection import app


class EventBus(object):
    def execute(self, event):
        event_handler = app.App().container.__getattribute__(
            event.__class__.__name__)()
        event_handler.handle(event)
