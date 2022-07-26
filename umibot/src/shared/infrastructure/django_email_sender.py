from typing import Any, Dict

from django.core.mail import send_mail
from src.shared.domain.email_sender import (
    EmailContent,
    EmailInfo,
    EmailSender,
    EmailTemplate,
)
from src.shared.domain.errors import InvalidEmailContentData


class DjangoEmailSender(EmailSender):
    def __init__(self, host_user: str) -> None:
        self.host_user = host_user

    def execute(
        self, info: EmailInfo, template: EmailTemplate, data: Dict[str, Any]
    ) -> None:
        email_content = self._get_email_content(template=template, data=data)
        send_mail(
            subject=email_content.subject,
            message=email_content.message,
            from_email=self.host_user,
            recipient_list=info.recipient_list,
        )

    def _get_email_content(
        self, template: EmailTemplate, data: Dict[str, Any]
    ) -> EmailContent:
        if template == EmailTemplate.WELCOME:
            username = data.get("name")
            if username is None:
                raise InvalidEmailContentData(
                    message="'name' is needed to welcome tamplate"
                )
            return EmailContent(
                subject="Welcome to UmiShop", message=f"Welcome {username}"
            )
        raise NotImplementedError(f"Template '{template}' is not implemented")
