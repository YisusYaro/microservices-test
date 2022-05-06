from shared.infraestructure.repositories.mongo_repository import MongoRepository
from resources.domain.factory import Factory


class ResourceRepository(MongoRepository):
    def __init__(self):
        super().__init__("resources")

    def save(self, resource):
        self.persist(resource)

    def find_by_id(self, id):
        document = self.collection().find_one({"_id": id})

        if(document is None):
            return None

        return self.document_to_resource(document)

    def document_to_resource(self, document):
        return Factory.reconstitute(id=document["_id"], name=document["name"], status=document["status"])
