import os

import pytest
from src.create_user.domain.email_sender import EmailInfo, EmailSender, EmailTemplate
from src.create_user.domain.errors import InvalidEmailContentData
from src.create_user.infrastructure.django_email_sender import DjangoEmailSender


@pytest.mark.integration
class TestEmailSender:
    email_info: EmailInfo
    email_sender: EmailSender

    def setup(self):
        self.email_info = EmailInfo(recipient_list=["fran.rodeno@gmail.com"])
        self.email_sender = DjangoEmailSender(host_user=os.getenv("EMAIL_HOST_USER"))

    def should_send_an_email_successfully(self):
        self.email_sender.execute(
            info=self.email_info,
            template=EmailTemplate.WELCOME,
            data={"name": "username"},
        )

    def should_raise_invalid_email_content_data(self):
        with pytest.raises(InvalidEmailContentData):
            self.email_sender.execute(
                info=self.email_info, template=EmailTemplate.WELCOME, data={}
            )
