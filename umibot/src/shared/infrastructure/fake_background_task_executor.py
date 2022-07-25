from typing import Any, Callable, Dict

from src.shared.domain.background_task_executor import BackgroundTaskExecutor


class FakeBackgroundTaskExecutor(BackgroundTaskExecutor):
    def execute(
        self, task: Callable[..., Any], parameters: Dict[str, Any] = {}
    ) -> None:
        pass
