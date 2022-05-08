import os
from datetime import datetime
from hashlib import md5

import requests
from characters.domain.factory import Factory


class CharacterHttpService(object):
    def __init__(self):
        self.__public_key = os.environ.get("MARVEL_PUBLIC_KEY")
        self.__private_key = os.environ.get("MARVEL_PRIVATE_KEY")
        self.__path = "https://gateway.marvel.com/v1/public/characters"
        self.__limit_pagination = 100

    def list_characters(self):
        offset = 0
        results = []

        while True:
            page_results, count = self.__fetch_page(offset)
            results = results = page_results
            offset += self.__limit_pagination
            if((count % self.__limit_pagination) != 0):
                break

        return list(map(self.__result_to_character, results))

    def __fetch_page(self, offset):
        http_result = self.__fetch(offset)

        json_result = http_result.json()

        return json_result["data"]["results"], json_result["data"]["count"]

    def __fetch(self, offset):
        timestamp = self.__get_timestamp()
        hash = self.__get_hash(timestamp)
        return requests.get(
            '{path}?limit={limit}&offset={offset}&ts={ts}&apikey={apikey}&hash={hash}'.format(path=self.__path, limit=self.__limit_pagination, offset=offset, ts=timestamp, apikey=self.__public_key, hash=hash))

    def __result_to_character(self, result):
        image = '{path}.{extension}'.format(
            path=result["thumbnail"]["path"], extension=result["thumbnail"]["extension"])

        appearances = result["stories"]["items"] + \
            result["events"]["items"] + result["series"]["items"]

        return Factory.reconstitute(id=result["id"], name=result["name"], image=image, appearances=appearances)

    def __get_hash(self, timestamp):
        return md5((timestamp+self.__private_key+self.__public_key).encode('utf-8')).hexdigest()

    def __get_timestamp(self):
        return str(datetime.timestamp(datetime.now()))
