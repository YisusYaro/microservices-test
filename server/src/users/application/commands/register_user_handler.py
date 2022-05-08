from users.infraestructure.repositories.user_respository import UserRepository
from shared.infraestructure.dependency_injection.app import App
from users.domain.factory import Factory

class RegisterUserHandler(object):
    def __init__(self, user_repository: UserRepository = App().container.UserRepository()):
        self.user_repository = user_repository

    def handle(self, command):

        user = self.user_repository.find_by_email(command.email)

        if(user != None):
            return

        user = Factory.create(
            id=self.user_repository.get_id(),
            name=command.name,
            email=command.email,
            age=command.age
        )

        user.openAccount(command.password)

        self.user_repository.save(user)

        user.commit()
