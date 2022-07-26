import uuid

from dependency_injector.wiring import Provide, inject
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import CharField, EmailField, UUIDField
from rest_framework.views import APIView
from src.api.exception_handler import UserAlreadyExistAPIException
from src.config.container import Container
from src.create_user.application.create_user import CreateUser
from src.create_user.domain.email_sender import EmailSender
from src.shared.domain.background_task_executor import BackgroundTaskExecutor
from src.shared.domain.user import User
from src.shared.domain.user_repository import UserRepository


class UserSerializer(serializers.Serializer[User]):
    public_id = UUIDField(required=False)
    name = CharField()
    email = EmailField()
    phone_number = CharField()
    origin = CharField()

    def to_domain_entity(self) -> User:
        if "public_id" not in self.data.keys() or self.data["public_id"] is None:
            return User(public_id=uuid.uuid4(), **self.data)
        return User.parse_obj(self.data)


class UserView(APIView):
    @inject
    @swagger_auto_schema(
        operation_description="Post endpoint to create users",
        request_body=UserSerializer,
        responses={
            UserAlreadyExistAPIException.status_code: UserAlreadyExistAPIException.detail
        },
    )
    def post(
        self,
        request: Request,
        user_repository: UserRepository = Provide[
            Container.repositories.user_repository
        ],
        email_sender: EmailSender = Provide[Container.services.email_sender],
        background_task_executor: BackgroundTaskExecutor = Provide[
            Container.services.background_task_executor
        ],
    ) -> Response:
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        CreateUser(
            user_repository=user_repository,
            email_sender=email_sender,
            background_task_executor=background_task_executor,
        ).execute(user=user_serializer.to_domain_entity())
        return Response(status=status.HTTP_201_CREATED)
