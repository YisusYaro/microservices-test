import bcrypt
from shared.domain.aggregate_root import AggregateRoot
from shared.domain.exceptions.bad_request import BadRequestException
from users.domain.errors.error import ErrorMessage
from users.domain.events.user_registered_event import UserRegisteredEvent


class User(AggregateRoot):
    def __init__(self, id, name, email, age, password=""):
        super().__init__()
        self.__id = id
        self.__name = name
        self.__email = email
        self.__age = age
        self.__password = password

    def toProperties(self):
        return dict(
            id=self.__id,
            name=self.__name,
            email=self.__email,
            age=self.__age,
            password=self.__password,
        )

    def openAccount(self, password):
        if(self.__password != ""):
            raise BadRequestException(ErrorMessage.CAN_NOT_SET_PASSWORD.value)

        self.__setPassword(password)

        event = UserRegisteredEvent(
            id=self.__id,
            name=self.__name,
        )

        self.record(event)

    def compare_password(self, password):
        return bcrypt.checkpw(
            password.encode(encoding='UTF-8', errors='strict'),
            self.__password
        )

    def __setPassword(self, password):
        if (password == ""):
            raise BadRequestException(ErrorMessage.CAN_NOT_SET_PASSWORD.value)
        self.__password = bcrypt.hashpw(
            password.encode(encoding='UTF-8', errors='strict'),
            bcrypt.gensalt()
        )
