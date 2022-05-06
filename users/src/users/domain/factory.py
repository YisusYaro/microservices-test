from users.domain.user import User


class Factory(object):
    @staticmethod
    def create(id, name, email, age):
        return User(id=id, name=name, email=email, age=age)

    @staticmethod
    def reconstitute(id, name, email, age, password):
        return User(id=id, name=name, email=email, age=age, password=password)
