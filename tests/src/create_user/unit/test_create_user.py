from unittest.mock import Mock

import pytest
from object_mothers.user_mother import UserMother
from src.create_user.application.create_user import CreateUser
from src.shared.domain.user import User
from src.shared.domain.user_repository import UserRepository


@pytest.mark.unit
class TestCreateUser:
    user: User
    mock_user_repository: UserRepository

    def setup(self):
        self.mock_user_repository = Mock(UserRepository)
        self.user = UserMother.random()

    def should_save_an_user_successfully(self):
        self.mock_user_repository.save = Mock(return_value=None)
        CreateUser(user_repository=self.mock_user_repository).execute(user=self.user)
        self.mock_user_repository.save.assert_called_once_with(user=self.user)
