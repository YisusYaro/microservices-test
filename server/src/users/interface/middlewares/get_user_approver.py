from shared.domain.exceptions.forbbiden import ForbbidenException
from shared.infrastructure.dependency_injection.app import App
from shared.infrastructure.tokens.token_service import TokenService


class GetUserApprover(object):
    def __init__(self, token_service: TokenService = App().container.TokenService()):
        self.__token_service = token_service

    def canExecute(self, token, id):
        payload = self.__token_service.verify(token)

        if(id != payload['id']):
            raise ForbbidenException('Forbbiden')
