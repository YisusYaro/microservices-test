from flask import Blueprint, request
from shared.infraestructure.dependency_injection.app import App

from users.application.commands.register_user_command import RegisterUserCommand
from users.application.queries.user_login_query import UserLoginQuery
from shared.domain.exceptions.unauthorized import UnauthorizedException

users_controller = Blueprint("users_controller", __name__)
command_bus = App().container.CommandBus()
query_bus = App().container.QueryBus()


@ users_controller.route("/users", methods=["POST"])
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


@ users_controller.route("/users/login", methods=["POST"])
def user_login():
    body = request.get_json()
    try:
        query = UserLoginQuery(
            email=body["email"],
            password=body["password"]
        )
        result = query_bus.execute(query)
        return result.__dict__, 200
    except UnauthorizedException as exception:
        return {"error": str(exception)}, 401
