class AuthException(Exception):
    pass


class UserNotFoundException(AuthException):
    pass


class InvalidEmailOrPasswordException(AuthException):
    pass
