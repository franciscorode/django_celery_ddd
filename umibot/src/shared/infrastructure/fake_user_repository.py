from src.shared.domain.user import User
from src.shared.domain.user_repository import UserRepository


class FakeUserRepository(UserRepository):
    def save(self, user: User) -> None:
        pass

    def clear(self) -> None:
        pass
