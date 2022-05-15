import os
from datetime import datetime
from hashlib import md5
from unittest import result

import requests
from shared.infrastructure.dependency_injection.app import App
from comics.domain.factory import Factory


class ComicHttpService(object):
    def __init__(self, filter=App().container.Filter()):
        self.__filter = filter
        self.__public_key = os.environ.get("MARVEL_PUBLIC_KEY")
        self.__private_key = os.environ.get("MARVEL_PRIVATE_KEY")
        self.__path = "https://gateway.marvel.com/v1/public/comics"
        self.__limit_pagination = 100
        self.__limit = 1000

    def list_comics_by_criteria(self, filters):
        if(len(filters) < 1):
            return self.__list_comics()
        return list(filter(lambda character: self.__filter.filter_by_criteria(filters, character), self.__list_comics()))

    def __list_comics(self):
        offset = 0
        results = []

        while True:
            page_results, count = self.__fetch_page(offset)
            results = results = page_results
            offset += self.__limit_pagination
            if((count % self.__limit_pagination) != 0 or count >= self.__limit_pagination):
                break

        return list(map(self.__result_to_character, results))

    def __fetch_page(self, offset):
        http_result = self.__fetch(offset)

        json_result = http_result.json()

        status = http_result.status_code

        print(status)

        if (status != 200):
            self.__fetch_page(offset)

        return json_result["data"]["results"], json_result["data"]["count"]

    def __fetch(self, offset):
        timestamp = self.__get_timestamp()
        hash = self.__get_hash(timestamp)
        return requests.get(
            '{path}?limit={limit}&offset={offset}&ts={ts}&apikey={apikey}&hash={hash}'.format(path=self.__path, limit=self.__limit_pagination, offset=offset, ts=timestamp, apikey=self.__public_key, hash=hash))

    def __result_to_character(self, result):

        image = '{path}.{extension}'.format(
            path=result["thumbnail"]["path"], extension=result["thumbnail"]["extension"])

        return Factory.reconstitute(id=result["id"], title=result["title"], image=image, on_sale_date=self.__get_on_sale_date(result["dates"]))
    
    def __get_on_sale_date(sale, dates):
        for date in dates:
            if date['type'] == "onsaleDate":
                return date['date']
        return ""

    def __get_hash(self, timestamp):
        return md5((timestamp+self.__private_key+self.__public_key).encode('utf-8')).hexdigest()

    def __get_timestamp(self):
        return str(datetime.timestamp(datetime.now()))
