from dependency_injector import providers


def set_queries(container):
    from characters.application.queries.list_characters_by_criteria_handler import ListCharactersByCriteriaHandler
    container.ListCharactersByCriteriaQuery = providers.Factory(
        ListCharactersByCriteriaHandler
    )


def set_application(container):
    set_queries(container)


def set_infrastructure(container):
    from characters.infrastructure.http_services.character_http_service import CharacterHttpService
    container.CharacterHttpService = providers.Factory(
        CharacterHttpService
    )


def set_characters_module(container):
    set_infrastructure(container)
    set_application(container)
