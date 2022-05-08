from ..dependency_injection import app


class CommandBus(object):
    def execute(self, command):
        command_handler = app.App().container.__getattribute__(
            command.__class__.__name__)()
        command_handler.handle(command)
