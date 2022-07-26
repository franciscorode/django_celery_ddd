from __future__ import annotations

from abc import ABC, abstractmethod

from pydantic import BaseModel


class NotificationMessage(BaseModel):
    title: str
    message: str


class Notifier(ABC):
    @abstractmethod
    def execute(self, message: NotificationMessage) -> None:
        raise NotImplementedError()
