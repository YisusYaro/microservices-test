from shared.infraestructure.dependency_injection.app import App
from characters.infraestructure.http_services.character_http_service import CharacterHttpService
from characters.application.queries.list_characters_by_criteria_result import ListCharactersByCriteriaResult


class GetUserHandler(object):
    def __init__(
        self,
        character_http_service: CharacterHttpService = App().container.CharacterHttpService(),
    ):
        self.character_http_service = character_http_service

    def handle(self, query):
        characters = self.character_http_service.list_characters_by_criteria(
            query.filters)

        print(characters)

        return ListCharactersByCriteriaResult("", "", "")
