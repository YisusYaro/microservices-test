import http.client


class CharacterHttpService(object):
    def __init__(self):
        self.__connection = http.client.HTTPSConnection(
            "gateway.marvel.com/v1/public/characters")
        self.__apikey = "e88d494087bf302528d097550fa4304b"

    def list_characters_by_criteria(self, filters):
        print("fetching")

        self.__connection.request(
            "GET", '/v1/public/characters?apikey={apikey}'.format(apikey=self.__apikey))

        response = self.__connection.getresponse()
        print("\n\n\n\n", response.read().decode())
