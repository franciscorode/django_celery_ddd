from typing import Any, Dict

from src.shared.domain.email_sender import EmailInfo, EmailSender, EmailTemplate


class FakeEmailSender(EmailSender):
    def execute(
        self, info: EmailInfo, template: EmailTemplate, data: Dict[str, Any]
    ) -> None:
        pass
