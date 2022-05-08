from characters.domain.character import Character


class Factory(object):
    @staticmethod
    def create(id, name, image, appearances):
        return Character(id=id, name=name, image=image, appearances=appearances)

    @staticmethod
    def reconstitute(id, name, image, appearances):
        return Character(id=id, name=name, image=image, appearances=appearances)
