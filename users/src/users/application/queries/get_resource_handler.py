from resources.application.queries.get_resource_result import GetResourceResult
from resources.infraestructure.repositories.resource_respository import \
    ResourceRepository
from shared.infraestructure.dependency_injection.app import App
from shared.domain.exceptions.bad_request import BadRequestException
from resources.domain.errors.error import ErrorMessage


class GetResourceHandler(object):
    def __init__(self, resource_repository: ResourceRepository = App().container.ResourceRepository()):
        self.resource_repository = resource_repository

    def handle(self, query):
        resource = self.resource_repository.find_by_id(query.id)

        if(resource is None):
            raise BadRequestException(ErrorMessage.RESOURCE_NOT_FOUND.value)

        properties = resource.toProperties()

        return GetResourceResult(name=properties['name'], status=properties['status'])
