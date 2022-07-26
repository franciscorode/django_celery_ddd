import os

import pytest
from src.customer_assistance.domain.notifier import NotificationMessage, Notifier
from src.customer_assistance.infrastructure.slack_notifier import SlackNotifier


@pytest.mark.skipif(
    condition=os.getenv("SLACK_TOKEN") is None, reason="Skip in local environments"
)
@pytest.mark.integration
class TestSlackNofifier:
    slack_notifier: Notifier

    def setup(self):
        slack_token = os.getenv("SLACK_TOKEN")
        slack_tests_channel = os.getenv("SLACK_TEST_CHANNEL", "testing")
        self.slack_notifier = SlackNotifier(
            token=slack_token, channel=slack_tests_channel
        )

    def should_send_a_notification_successfully(self):
        notifier_message = NotificationMessage(title="Test title", message="message")
        self.slack_notifier.execute(message=notifier_message)
