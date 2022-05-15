from shared.infrastructure.dependency_injection.app import App
from users.application.queries.get_user_result import GetUserResult
from users.domain.errors.error import ErrorMessage
from users.infrastructure.repositories.user_respository import UserRepository
from users.infrastructure.tokens.user_token_service import UserTokenService
from shared.domain.exceptions.bad_request import BadRequestException


class GetUserHandler(object):
    def __init__(
        self,
        user_repository: UserRepository = App().container.UserRepository(),
        user_token_service: UserTokenService = App().container.UserTokenService(),
    ):
        self.user_repository = user_repository
        self.user_token_service = user_token_service

    def handle(self, query):
        user = self.user_repository.find_by_id(query.id)

        if(user is None):
            raise BadRequestException(
                ErrorMessage.USER_NOT_FOUND.value)

        properties = user.toProperties()

        return GetUserResult(name=properties["name"], email=properties["email"], age=properties["age"])
