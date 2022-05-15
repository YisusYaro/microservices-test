from users.application.queries.user_login_result import UserLoginResult
from users.infrastructure.repositories.user_respository import \
    UserRepository
from users.infrastructure.tokens.user_token_service import UserTokenService
from shared.infrastructure.dependency_injection.app import App
from shared.domain.exceptions.unauthorized import UnauthorizedException
from users.domain.errors.error import ErrorMessage


class UserLoginHandler(object):
    def __init__(
        self,
        user_repository: UserRepository = App().container.UserRepository(),
        user_token_service: UserTokenService = App().container.UserTokenService(),
    ):
        self.user_repository = user_repository
        self.user_token_service = user_token_service

    def handle(self, query):
        user = self.user_repository.find_by_email(query.email)

        if(user is None):
            raise UnauthorizedException(
                ErrorMessage.USER_NOT_FOUND_OR_NOT_AUTHORIZED.value)

        if(not user.compare_password(query.password)):
            raise UnauthorizedException(
                ErrorMessage.USER_NOT_FOUND_OR_NOT_AUTHORIZED.value)

        token = self.user_token_service.get_authorization_token(
            user.toProperties()['id'])

        return UserLoginResult(Authorization=token)
