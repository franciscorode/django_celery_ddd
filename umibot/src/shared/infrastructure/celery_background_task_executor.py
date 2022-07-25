from datetime import datetime, timedelta
from typing import Any, Callable, Dict

from src import celery_app
from src.shared.domain.background_task_executor import BackgroundTaskExecutor


@celery_app.task
def task_wrapper(task: Callable[..., Any], parameters: Dict[str, Any]) -> None:
    try:
        task(**parameters)
    except TypeError as e:
        raise TypeError(
            f"Error running {str(task)} with parameters {parameters}. Message: {str(e)}"
        )
    except Exception as e:
        raise Exception(
            f"Error running {str(task)} with parameters {parameters}. Message: {str(e)}"
        )


class CeleryBackgroundTaskExecutor(BackgroundTaskExecutor):
    def __init__(self, eta_seconds: int) -> None:
        self.eta_seconds: int = eta_seconds

    def execute(
        self, task: Callable[..., Any], parameters: Dict[str, Any] = {}
    ) -> None:
        task_wrapper.apply_async(
            kwargs={"task": task, "parameters": parameters},
            eta=datetime.now() + timedelta(seconds=self.eta_seconds),
        )
