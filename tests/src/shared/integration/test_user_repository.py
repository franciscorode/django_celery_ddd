import pytest
from object_mothers.user_mother import UserMother
from src.create_user.domain.errors import UserAlreadyExist
from src.shared.domain.user import User
from src.shared.domain.user_repository import UserRepository
from src.shared.infrastructure.sql_django_user_repository import SqlDjangoUserRepository


@pytest.mark.django_db
@pytest.mark.integration
class TestUserRepository:
    user: User
    user_repository: UserRepository

    def setup(self):
        self.user = UserMother.random()
        self.user_repository = SqlDjangoUserRepository()

    def teardown(self):
        self.user_repository.clear()

    def should_save_an_user_successfully(self):
        self.user_repository.save(user=self.user)

    def should_raise_user_already_exist_error(self):
        self.user_repository.save(user=self.user)
        with pytest.raises(UserAlreadyExist):
            self.user_repository.save(user=self.user)
