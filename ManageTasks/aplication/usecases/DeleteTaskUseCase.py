from ManageTasks.domain.ports.taskport import TaskPort


class DeleteUseCase:
    def __init__(self, task_port: TaskPort):
        self.repository = task_port

    def run(self, id):
        self.repository.delete_task(id)
