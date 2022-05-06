from resources.infraestructure.repositories.resource_respository import ResourceRepository
from shared.infraestructure.dependency_injection.app import App
from resources.domain.factory import Factory


class ResourceCreatedHandler(object):
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
            "status: ", event.status, "\n",
        )
