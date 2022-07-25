from abc import ABC, abstractmethod
from typing import Any, Callable, Dict


class BackgroundTaskExecutor(ABC):
    @abstractmethod
    def execute(
        self, task: Callable[..., Any], parameters: Dict[str, Any] = {}
    ) -> None:
        raise NotImplementedError()
