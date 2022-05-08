from shared.infraestructure.repositories.mongo_client_factory import MongoClientFactory


class MongoRepository(object):
    def __init__(self, collection_name):
        self.__client = MongoClientFactory.connect()
        self.collection_name = collection_name

    def collection(self):
        return self.__client[self.collection_name]

    def persist(self, aggregateRoot):
        properties = aggregateRoot.toProperties()
        aggregateId = properties["id"]
        del properties["id"]
        self.collection().update_one(
            {'_id': aggregateId}, {'$set': properties}, upsert=True)
