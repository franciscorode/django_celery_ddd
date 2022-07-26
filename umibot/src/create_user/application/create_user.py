from src.shared.domain.background_task_executor import BackgroundTaskExecutor
from src.shared.domain.email_sender import EmailInfo, EmailSender, EmailTemplate
from src.shared.domain.user import User
from src.shared.domain.user_repository import UserRepository


class CreateUser:
    def __init__(
        self,
        user_repository: UserRepository,
        email_sender: EmailSender,
        background_task_executor: BackgroundTaskExecutor,
    ) -> None:
        self.user_repository = user_repository
        self.email_sender = email_sender
        self.background_task_executor = background_task_executor

    def execute(self, user: User) -> None:
        self.user_repository.save(user=user)
        self.background_task_executor.execute(
            task=self.email_sender.execute,
            parameters={
                "info": EmailInfo(recipient_list=[user.email]),
                "template": EmailTemplate.WELCOME,
                "data": {"name": user.name},
            },
        )
