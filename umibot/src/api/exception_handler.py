from typing import Any, Optional

from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import exception_handler

from src.create_user.domain.errors import UserAlreadyExist


class HttpAPIException(APIException):
    def to_response(self) -> Response:
        return Response({"message": self.detail}, status=self.status_code)


class UserAlreadyExistAPIException(HttpAPIException):
    status_code = status.HTTP_409_CONFLICT
    detail = "User already exist"


def custom_exception_handler(
    exc: Exception, context: dict[str, Any]
) -> Optional[Response]:
    response = exception_handler(exc, context)

    if isinstance(exc, UserAlreadyExist):
        return UserAlreadyExistAPIException().to_response()

    return response
