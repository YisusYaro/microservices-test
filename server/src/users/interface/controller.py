from functools import wraps
from re import A
from flask import Blueprint, request
from shared.infrastructure.dependency_injection.app import App
from shared.interface.handle_http_error import handle_http_error

from users.application.commands.register_user_command import RegisterUserCommand
from users.application.queries.user_login_query import UserLoginQuery
from users.application.queries.get_user_query import GetUserQuery
from users.interface.middlewares.get_user_middleware import get_user_middleware


users_controller = Blueprint("users_controller", __name__)
command_bus = App().container.CommandBus()
query_bus = App().container.QueryBus()


@users_controller.route("/users", methods=["POST"])
@handle_http_error()
def register_user():
    body = request.get_json()
    command = RegisterUserCommand(
        name=body["name"],
        email=body["email"],
        age=body["age"],
        password=body["password"]
    )
    command_bus.execute(command)
    return {}, 204


@users_controller.route("/users/login", methods=["POST"])
@handle_http_error()
def user_login():
    body = request.get_json()
    query = UserLoginQuery(
        email=body["email"],
        password=body["password"]
    )
    result = query_bus.execute(query)
    return result.__dict__, 200


@users_controller.route("/users/<id>", methods=["GET"])
@handle_http_error()
@get_user_middleware
def get_user(id):
    id = request.view_args["id"]
    query = GetUserQuery(
        id=id
    )
    result = query_bus.execute(query)
    return result.__dict__, 200
