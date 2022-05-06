from resources.domain.resource import Resource


class Factory(object):
    @staticmethod
    def create(id, name):
        return Resource(id=id, name=name)

    @staticmethod
    def reconstitute(id, name, status):
        return Resource(id=id, name=name, status=status)
