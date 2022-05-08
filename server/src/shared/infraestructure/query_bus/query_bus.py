from ..dependency_injection import app


class QueryBus(object):
    def execute(self, query):
        query_handler = app.App().container.__getattribute__(
            query.__class__.__name__)()
        result = query_handler.handle(query)
        return result
