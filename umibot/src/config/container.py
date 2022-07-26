import os

from dependency_injector import containers, providers
from dotenv import load_dotenv
from src.customer_assistance.domain.notifier import Notifier
from src.customer_assistance.infrastructure.fake_notifier import FakeNotifier
from src.customer_assistance.infrastructure.slack_notifier import SlackNotifier
from src.shared.domain.background_task_executor import BackgroundTaskExecutor
from src.shared.domain.email_sender import EmailSender
from src.shared.domain.user_repository import UserRepository
from src.shared.infrastructure.celery_background_task_executor import (
    CeleryBackgroundTaskExecutor,
)
from src.shared.infrastructure.django_email_sender import DjangoEmailSender
from src.shared.infrastructure.fake_background_task_executor import (
    FakeBackgroundTaskExecutor,
)
from src.shared.infrastructure.fake_email_sender import FakeEmailSender
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

    # Email sender
    email_sender_type = os.getenv("EMAIL_SENDER_TYPE")
    email_host_user = os.getenv("EMAIL_HOST_USER")
    if email_sender_type != "fake" and not email_host_user:
        raise RuntimeError(
            "Environment variable 'EMAIL_HOST_USER' is necessary to start the application"
        )
    email_sender: providers.Provider[EmailSender] = (
        providers.Factory(DjangoEmailSender, host_user=email_host_user)
        if email_sender_type != "fake"
        else providers.Factory(FakeEmailSender)
    )

    # Task executor
    background_task_executor: providers.Provider[BackgroundTaskExecutor] = (
        providers.Factory(CeleryBackgroundTaskExecutor, eta_seconds=0)
        if os.getenv("BACKGROUND_TASK_EXECUTOR_TYPE") != "fake"
        else providers.Factory(FakeBackgroundTaskExecutor)
    )

    # Notifier
    notifier_type = os.getenv("NOTIFIER_TYPE")
    slack_channel = os.getenv("SLACK_CHANNEL")
    slack_token = os.getenv("SLACK_TOKEN")
    if notifier_type == "slack" and (not slack_channel or not slack_token):
        raise RuntimeError(
            "Environment variables 'SLACK_CHANNEL' and 'SLACK_TOKEN' are necessary to"
            " start the application"
        )
    notifier: providers.Provider[Notifier] = (
        providers.Factory(SlackNotifier, token=slack_token, channel=slack_channel)
        if notifier_type == "slack"
        else providers.Factory(FakeNotifier)
    )


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    services = providers.Container(Services)
    repositories = providers.Container(Repositories)
