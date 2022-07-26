import os

from src.customer_assistance.domain.customer_request import CustomerRequest, Department
from src.customer_assistance.domain.notifier import NotificationMessage, Notifier
from src.shared.domain.email_sender import EmailInfo, EmailSender, EmailTemplate


class AssistCustomer:
    def __init__(
        self,
        email_sender: EmailSender,
        notifier: Notifier,
    ) -> None:
        self.email_sender = email_sender
        self.notifier = notifier
        if os.getenv("CUSTOMER_SUPPORT_EMAIL") is None:
            raise RuntimeError(
                "Environment variable 'CUSTOMER_SUPPORT_EMAIL' is necessary to "
                "can assist to customers"
            )
        self.customer_support_email = os.getenv("CUSTOMER_SUPPORT_EMAIL")

    def execute(self, customer_request: CustomerRequest) -> None:
        if customer_request.department == Department.SALES:
            self.notifier.execute(
                message=NotificationMessage(
                    title="Customer request", message=customer_request.question
                )
            )
        if customer_request.department == Department.PRICING:
            self.email_sender.execute(
                info=EmailInfo(recipient_list=[self.customer_support_email]),
                template=EmailTemplate.CUSTOMER_REQUEST,
                data={"question": customer_request.question},
            )
