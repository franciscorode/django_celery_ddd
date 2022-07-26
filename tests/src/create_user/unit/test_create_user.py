from unittest.mock import Mock

import pytest
from object_mothers.user_mother import UserMother
from src.create_user.application.create_user import CreateUser
from src.create_user.domain.email_sender import EmailSender
from src.create_user.domain.errors import UserAlreadyExist
from src.shared.domain.background_task_executor import BackgroundTaskExecutor
from src.shared.domain.user import User
from src.shared.domain.user_repository import UserRepository


@pytest.mark.unit
class TestCreateUser:
    user: User
    mock_user_repository: UserRepository
    mock_email_sender: EmailSender
    mock_task_executor: BackgroundTaskExecutor

    def setup(self):
        self.mock_user_repository = Mock(UserRepository)
        self.mock_email_sender = Mock(EmailSender)
        self.mock_task_executor = Mock(BackgroundTaskExecutor)
        self.user = UserMother.random()

    def should_save_an_user_successfully(self):
        self.mock_user_repository.save = Mock(return_value=None)
        self.mock_task_executor.execute = Mock(return_value=None)
        CreateUser(
            user_repository=self.mock_user_repository,
            email_sender=self.mock_email_sender,
            background_task_executor=self.mock_task_executor,
        ).execute(user=self.user)
        self.mock_user_repository.save.assert_called_once_with(user=self.user)
        self.mock_task_executor.execute.assert_called_once()

    def should_not_execute_send_email_task_when_save_user_raise_an_exception(self):
        self.mock_user_repository.save.side_effect = UserAlreadyExist()
        with pytest.raises(UserAlreadyExist):
            CreateUser(
                user_repository=self.mock_user_repository,
                email_sender=self.mock_email_sender,
                background_task_executor=self.mock_task_executor,
            ).execute(user=self.user)
        self.mock_user_repository.save.assert_called_once_with(user=self.user)
        self.mock_task_executor.execute.assert_not_called()
