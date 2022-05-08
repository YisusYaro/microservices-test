from functools import wraps
from shared.domain.exceptions.unauthorized import UnauthorizedException
from shared.domain.exceptions.bad_request import BadRequestException
from shared.domain.exceptions.forbbiden import ForbbidenException


def handle_http_error():
    def _handle_http_error(f):
        @wraps(f)
        def __handle_http_error(*args, **kwargs):
            try:
                result = f(*args, **kwargs)
                return result
            except BadRequestException as exception:
                return {"error": str(exception)}, 400
            except UnauthorizedException as exception:
                return {"error": str(exception)}, 401
            except ForbbidenException as exception:
                return {"error": str(exception)}, 403
            except:
                return {"error": str(exception)}, 500
        return __handle_http_error
    return _handle_http_error
