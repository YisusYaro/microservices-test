from dependency_injector import providers


def set_queries(container):
    from comics.application.queries.list_comics_by_criteria_handler import ListComicsByCriteriaHandler
    container.ListComicsByCriteriaQuery = providers.Factory(
        ListComicsByCriteriaHandler
    )


def set_application(container):
    set_queries(container)


def set_infrastructure(container):
    from comics.infrastructure.http_services.comic_http_service import ComicHttpService
    container.ComicHttpService = providers.Factory(
        ComicHttpService
    )


def set_comics_module(container):
    set_infrastructure(container)
    set_application(container)
