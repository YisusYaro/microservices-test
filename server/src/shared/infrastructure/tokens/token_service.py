import os

import jwt
from shared.domain.exceptions.unauthorized import UnauthorizedException


class TokenService(object):
    def verify(self, token):
        try:
            return jwt.decode(token, os.environ.get("JWT_SECRET"), algorithms=["HS256"])
        except:
            raise UnauthorizedException("Invalid token")

