from ManageTasks.domain.ports.taskport import TaskPort
from ManageTasks.domain.entities.tasks import Tasks


class CreateUseCase:
    def __init__(self, task_port: TaskPort):
        self.repository = task_port

    def run(self, data):
        task = Tasks(name=data["name"], description=data["description"], status=data["status"])
        return self.repository.create_task(task)
