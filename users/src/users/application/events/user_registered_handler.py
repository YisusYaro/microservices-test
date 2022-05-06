from users.infraestructure.repositories.user_respository import UserRepository
from shared.infraestructure.dependency_injection.app import App

class UserRegisteredHandler(object):
    def handle(self, event):
        print(
            '\x1b[6;30;42m',
            "info",
            '\x1b[0m', "\n",
            "event_name: ", event.event_name, "\n",
            "aggregate_id", event.aggregate_id, "\n",
            "event_id: ", event.event_id, "\n",
            "ocurred_on: ", event.ocurred_on, "\n",
            "id: ", event.id, "\n",
            "name: ", event.name, "\n",
        )
