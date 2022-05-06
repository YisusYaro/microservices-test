import enum


class ErrorMessage(enum.Enum):
    USER_NOT_FOUND = 'User not found'
    USER_NOT_FOUND_OR_NOT_AUTHORIZED = 'User not found or not authorized'
    CAN_NOT_SET_PASSWORD = 'Can not set password'
