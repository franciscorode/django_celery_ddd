from dependency_injector.wiring import Provide, inject
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import CharField, ChoiceField
from rest_framework.views import APIView
from src.config.container import Container
from src.customer_assistance.application.assist_customer import AssistCustomer
from src.customer_assistance.domain.customer_request import CustomerRequest, Department
from src.customer_assistance.domain.notifier import Notifier
from src.shared.domain.email_sender import EmailSender


class CustomerRequestSerializer(serializers.Serializer[CustomerRequest]):
    department = ChoiceField(choices=Department.get_values())
    question = CharField()

    def to_domain_entity(self) -> CustomerRequest:
        return CustomerRequest.parse_obj(self.data)


class CustomerRequestView(APIView):
    @inject
    @swagger_auto_schema(
        operation_description="Post endpoint to request customer assistance",
        request_body=CustomerRequestSerializer,
    )
    def post(
        self,
        request: Request,
        email_sender: EmailSender = Provide[Container.services.email_sender],
        notifier: Notifier = Provide[Container.services.notifier],
    ) -> Response:
        request_serializer = CustomerRequestSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        AssistCustomer(email_sender=email_sender, notifier=notifier).execute(
            customer_request=request_serializer.to_domain_entity()
        )
        return Response(status=status.HTTP_201_CREATED)
