import json
from unittest.mock import patch

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from object_mothers.user_mother import UserMother
from src.create_user.domain.errors import UserAlreadyExist
from src.shared.domain.user import User
from src.shared.infrastructure.fake_user_repository import FakeUserRepository


@pytest.mark.acceptance
class TestPostUser:
    user: User
    client: APIClient
    url: str

    def setup(self):
        self.user = UserMother.random()
        self.client = APIClient()
        self.url = reverse("user")

    def should_post_user_should_return_201_status_code(self):
        response = self.client.post(
            self.url, self.user.json(), content_type="application/json"
        )
        assert response.status_code == status.HTTP_201_CREATED

    def should_post_user_should_return_201_status_code_generating_public_id_in_backend(
        self,
    ):
        data = self.user.dict()
        del data["public_id"]
        response = self.client.post(
            self.url, json.dumps(data), content_type="application/json"
        )
        assert response.status_code == status.HTTP_201_CREATED

    def should_return_400_status_code_when_body_is_invalid(self):
        response = self.client.post(self.url, "{}", content_type="application/json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def should_return_409_status_code_when_an_user_already_exist(self):
        with patch.object(FakeUserRepository, "save", side_effect=UserAlreadyExist()):
            response = self.client.post(
                self.url, self.user.json(), content_type="application/json"
            )
        assert response.status_code == status.HTTP_409_CONFLICT
