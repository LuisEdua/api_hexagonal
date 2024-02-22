from typing import Any

from ..entities.tasks import Tasks
from abc import ABC, abstractmethod

class TaskPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_tasks(self) -> Any:
        pass

    @abstractmethod
    def create_task(self, task: Tasks) -> Any:
        pass

    @abstractmethod
    def update_task(self, id, name) -> Any:
        pass

    @abstractmethod
    def delete_task(self, id):
        pass
