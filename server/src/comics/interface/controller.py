import json

from comics.application.queries.list_comics_by_criteria_query import \
    ListComicsByCriteriaQuery
from flask import Blueprint, request
from shared.infrastructure.dependency_injection.app import App
from shared.interface.handle_http_error import handle_http_error

comics_controller = Blueprint("comics_controller", __name__)
query_bus = App().container.QueryBus()


@comics_controller.route("/comics/", methods=["GET"])
@handle_http_error()
def list_comics_by_criteria():
    raw_filters = request.args.getlist('filters')

    formated_filters = list(map(format_filter, raw_filters))

    query = ListComicsByCriteriaQuery(
        filters=formated_filters,
    )
    result = query_bus.execute(query)

    return result.__dict__, 200


def format_filter(filter):
    return json.loads(filter)
