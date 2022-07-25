import os

import pytest
from src.shared.domain.background_task_executor import BackgroundTaskExecutor
from src.shared.infrastructure.celery_background_task_executor import (
    CeleryBackgroundTaskExecutor,
)


def is_redis_available():
    import redis

    r = redis.Redis.from_url(url=os.getenv("CELERY_BROKER"))
    try:
        r.ping()
    except (redis.exceptions.ConnectionError, ConnectionRefusedError):
        return False
    return True


def fuction_1(param1: str):
    pass


@pytest.mark.skipif(
    condition=not is_redis_available(),
    reason="Skipped because redis is not reachable",
)
@pytest.mark.integration
class TestBackgroundTaskExecutor:
    task_executor: BackgroundTaskExecutor

    def setup(self):
        self.task_executor = CeleryBackgroundTaskExecutor(eta_seconds=0)

    def should_execute_a_task_in_background_successfully(self):
        self.task_executor.execute(task=fuction_1, parameters={"param1": "param1"})
