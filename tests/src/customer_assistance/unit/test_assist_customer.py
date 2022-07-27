from unittest.mock import Mock

import pytest

from src.customer_assistance.application.assist_customer import AssistCustomer
from src.customer_assistance.domain.notifier import Notifier
from src.shared.domain.email_sender import EmailSender
from tests.object_mothers.customer_request_mother import CustomerRequestMother


@pytest.mark.unit
class TestAssistCustomer:
    mock_notifier: Notifier
    mock_email_sender: EmailSender

    def setup(self):
        self.mock_email_sender = Mock(EmailSender)
        self.mock_notifier = Mock(Notifier)

    def should_notify_question_when_request_is_for_sales_department(self):
        self.mock_notifier.execute = Mock(return_value=None)

        AssistCustomer(
            notifier=self.mock_notifier, email_sender=self.mock_email_sender
        ).execute(customer_request=CustomerRequestMother.sales_request())

        self.mock_notifier.execute.assert_called_once()
        self.mock_email_sender.execute.assert_not_called()

    def should_send_question_by_email_when_request_is_for_pricing_department(self):
        self.mock_email_sender.execute = Mock(return_value=None)

        AssistCustomer(
            notifier=self.mock_notifier, email_sender=self.mock_email_sender
        ).execute(customer_request=CustomerRequestMother.pricing_request())

        self.mock_email_sender.execute.assert_called_once()
        self.mock_notifier.execute.assert_not_called()
