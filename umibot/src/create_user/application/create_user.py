from src.shared.domain.user import User
from src.shared.domain.user_repository import UserRepository


class CreateUser:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def execute(self, user: User) -> None:
        self.user_repository.save(user=user)
