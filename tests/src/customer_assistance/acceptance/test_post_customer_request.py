import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from object_mothers.customer_request_mother import CustomerRequestMother
from src.customer_assistance.domain.customer_request import CustomerRequest


@pytest.mark.acceptance
class TestPostCustomerRequest:
    customer_request: CustomerRequest
    client: APIClient
    url: str

    def setup(self):
        self.customer_request = CustomerRequestMother.random()
        self.client = APIClient()
        self.url = reverse("customer-request")

    def should_post_a_customer_request_and_return_201_status_code(self):
        response = self.client.post(
            self.url, self.customer_request.json(), content_type="application/json"
        )
        assert response.status_code == status.HTTP_201_CREATED

    def should_return_400_status_code_when_customer_request_body_is_invalid(self):
        response = self.client.post(self.url, "{}", content_type="application/json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
