import os

import pymongo
from pymongo import MongoClient


class MongoClientFactory(object):
    @staticmethod
    def connect():
        CONNECTION_STRING = 'mongodb+srv://{user}:{password}@{database_host}/{database}?retryWrites=true&w=majority'.format(
            user=os.environ.get("DATABASE_USER"),
            password=os.environ.get("DATABASE_PASSWORD"),
            database_host=os.environ.get("DATABASE_HOST"),
            database=os.environ.get("DATABASE")
        )
        client = MongoClient(CONNECTION_STRING)
        return client["resources-database"]
