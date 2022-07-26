from src.customer_assistance.domain.notifier import NotificationMessage, Notifier


class FakeNotifier(Notifier):
    def execute(self, message: NotificationMessage) -> None:
        pass
