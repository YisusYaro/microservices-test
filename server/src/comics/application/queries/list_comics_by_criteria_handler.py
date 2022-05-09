from shared.infraestructure.dependency_injection.app import App
from comics.infraestructure.http_services.comic_http_service import ComicHttpService
from comics.application.queries.list_comics_by_criteria_result import ListComicsByCriteriaResult


class ListComicsByCriteriaHandler(object):
    def __init__(
        self,
        character_http_service: ComicHttpService = App().container.ComicHttpService(),
    ):
        self.character_http_service = character_http_service

    def handle(self, query):
        comics = self.character_http_service.list_comics_by_criteria(query.filters)

        return ListComicsByCriteriaResult(list(map(self.__character_to_properties, comics)))

    def __character_to_properties(self, character):
        return character.to_properties()
