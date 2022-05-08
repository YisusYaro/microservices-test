import json

from characters.application.queries.list_characters_by_criteria_query import \
    ListCharactersByCriteriaQuery
from flask import Blueprint, request
from shared.infraestructure.dependency_injection.app import App
from shared.interface.handle_http_error import handle_http_error

shared_controller = Blueprint("shared_controller", __name__)
query_bus = App().container.QueryBus()


@shared_controller.route("/searchComics/", methods=["GET"])
@handle_http_error()
def list_characters_by_criteria():
    raw_filters = request.args.getlist('filters')

    formated_filters = map(format_filter, raw_filters)
    
    query = ListCharactersByCriteriaQuery(
        filters=formated_filters,
    )
    result = query_bus.execute(query)
    return result.__dict__, 200

def format_filter(filter):
    return json.loads(filter)