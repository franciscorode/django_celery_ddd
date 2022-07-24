from src.create_user.domain.errors import UserAlreadyExist
from src.shared.domain.user import User
from src.shared.domain.user_repository import UserRepository
from src.shared.infrastructure.models import SqlUser


class SqlDjangoUserRepository(UserRepository):
    def save(self, user: User) -> None:
        if SqlUser.objects.filter(username=user.name).exists():
            raise UserAlreadyExist()
        sql_user = SqlUser.from_domain_entity(user=user)
        sql_user.save()

    def clear(self) -> None:
        SqlUser.objects.all().delete()
