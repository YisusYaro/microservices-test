from flask import Blueprint, Response, jsonify, request
from resources.application.queries.get_resource_query import GetResourceQuery
from shared.domain.exceptions.bad_request import BadRequestException
from shared.infraestructure.dependency_injection.app import App

from ..application.commands.create_resource_command import \
    CreateResourceCommand

resources_controller = Blueprint("resources_controller", __name__)
command_bus = App().container.CommandBus()
query_bus = App().container.QueryBus()


@resources_controller.route("/resources/<id>", methods=["GET"])
def get_resource(id):
    id = request.view_args["id"]
    try:
        query = GetResourceQuery(id)
        result = query_bus.execute(query)
        return result.__dict__, 200
    except BadRequestException as exception:
        return {"error": str(exception)}, 404


@ resources_controller.route("/resources", methods=["POST"])
def create_resource():
    body = request.get_json()
    command = CreateResourceCommand(id=body["id"], name=body["name"])
    command_bus.execute(command)
    return {}, 204
