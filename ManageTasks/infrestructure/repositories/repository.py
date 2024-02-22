from typing import Any

from ManageTasks.domain.ports.taskport import TaskPort
from ManageTasks.domain.entities.tasks import Tasks

class Repository(TaskPort):
    def __init__(self):
        self.session = []

    def get_tasks(self) -> Any:
        return self.session

    def create_task(self, task: Tasks) -> Any:
        self.session.append(task)
        return task

    def update_task(self, id, name) -> Any:
        task = next((task for task in self.session if task.id == id), None)
        if task is not None:
            task.name = name
            return task

    def delete_task(self, id):
        task = next((i for i, task in enumerate(self.session) if task.id == id), None)
        if task is not None:
            self.session.pop(task)