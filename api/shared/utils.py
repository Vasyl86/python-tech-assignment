from enum import Enum

class HTTPStatus(Enum):
    OK = 200
    CREATED = 201
    NO_CONTENT = 204
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500
    UNAUTHORIZED = 401

class RequestStatus(Enum):
    Pending = 'Pending'
    Completed = 'Completed'
    Rejected = 'Rejected'