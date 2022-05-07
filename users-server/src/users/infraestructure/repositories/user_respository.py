import ulid
from shared.infraestructure.repositories.mongo_repository import \
    MongoRepository
from users.domain.factory import Factory


class UserRepository(MongoRepository):
    def __init__(self):
        super().__init__("users")

    def get_id(self):
        id = ulid.new()
        return id.str

    def save(self, user):
        self.persist(user)

    def find_by_id(self, id):
        document = self.collection().find_one({"_id": id})

        if(document is None):
            return None

        return self.document_to_user(document)

    def find_by_email(self, email):
        document = self.collection().find_one({"email": email})

        if(document is None):
            return None

        return self.document_to_user(document)

    def document_to_user(self, document):
        return Factory.reconstitute(
            id=document["_id"],
            name=document["name"],
            email=document["email"],
            age=document["age"],
            password=document["password"]
        )
