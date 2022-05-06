import os

import jwt


class UserTokenService(object):
    def get_authorization_token(self, id):
        return jwt.encode({"id": id}, os.environ.get("JWT_SECRET"), algorithm="HS256")
