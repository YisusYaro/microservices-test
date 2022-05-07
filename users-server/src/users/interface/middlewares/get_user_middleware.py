from functools import wraps
from flask import request

from shared.infraestructure.dependency_injection.app import App


def get_user_middleware(f):
    @wraps(f)
    def __get_user_middleware(*args, **kwargs):
        try:
            token = request.headers['Authorization']
            id = request.view_args["id"]
        except:
            pass
        approver = App().container.GetUserApprover()
        approver.canExecute(token=token, id=id)
        result = f(*args, **kwargs)
        return result
    return __get_user_middleware
