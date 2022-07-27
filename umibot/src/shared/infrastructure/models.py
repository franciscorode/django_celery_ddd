from __future__ import annotations

import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from src.shared.domain.user import User


class SqlUser(AbstractUser):
    phone_number = models.CharField(max_length=30)
    origin = models.CharField(max_length=40)
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    @staticmethod
    def from_domain_entity(user: User) -> SqlUser:
        return SqlUser(
            username=user.name,
            email=user.email,
            phone_number=user.phone_number,
            origin=user.origin,
            public_id=user.public_id,
        )

    def to_domain_entity(self) -> User:
        return User(
            name=self.username,
            email=self.email,
            phone_number=self.phone_number,
            origin=self.origin,
            public_id=self.public_id,
        )
