from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Dict, List

from pydantic import BaseModel

from src.shared.domain.user import User


class EmailContent(BaseModel):
    subject: str
    message: str


class EmailTemplate(Enum):
    WELCOME = "WELCOME"
    CUSTOMER_REQUEST = "CUSTOMER_REQUEST"


class EmailInfo(BaseModel):
    recipient_list: List[str]

    @staticmethod
    def from_user(user: User) -> EmailInfo:
        return EmailInfo(recipient_list=[user.email])


class EmailSender(ABC):
    @abstractmethod
    def execute(
        self, info: EmailInfo, template: EmailTemplate, data: Dict[str, Any]
    ) -> None:
        raise NotImplementedError()
