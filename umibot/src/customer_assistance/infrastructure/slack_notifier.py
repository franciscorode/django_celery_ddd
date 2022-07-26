from typing import Any, Dict, List

from slack_sdk.errors import SlackApiError
from slack_sdk.web.client import WebClient
from src.customer_assistance.domain.notifier import NotificationMessage, Notifier

SLACK_MAX_LENGHT = 3000


class SlackError(Exception):
    pass


class SlackNotifier(Notifier):
    def __init__(self, token: str, channel: str):
        self.channel = channel
        self.client = WebClient(token=token)

    def execute(self, message: NotificationMessage) -> None:
        try:
            self.client.chat_postMessage(
                channel=self.channel,
                blocks=self._parse_message(message=message),
                text=message.title,
            )
        except SlackApiError as exception:
            raise SlackError(exception.response["error"]) from exception

    def _parse_message(self, message: NotificationMessage) -> List[Dict[str, Any]]:
        header_block = {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": message.title,
                "emoji": True,
            },
        }
        message_block = message_block = {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": message.message[:SLACK_MAX_LENGHT],
            },
        }
        divider_block = {"type": "divider"}
        return [header_block, message_block, divider_block]
