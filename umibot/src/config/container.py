import os

from dependency_injector import containers, providers
from dotenv import load_dotenv
from src.shared.domain.user_repository import UserRepository
from src.shared.infrastructure.fake_user_repository import FakeUserRepository
from src.shared.infrastructure.sql_django_user_repository import SqlDjangoUserRepository

load_dotenv()


class Repositories(containers.DeclarativeContainer):

    config = providers.Configuration()

    user_repository: providers.Provider[UserRepository] = (
        providers.Factory(SqlDjangoUserRepository)
        if os.getenv("USER_REPOSITORY_TYPE") != "fake"
        else providers.Factory(FakeUserRepository)
    )


class Services(containers.DeclarativeContainer):
    config = providers.Configuration()


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    services = providers.Container(Services)
    repositories = providers.Container(Repositories)
