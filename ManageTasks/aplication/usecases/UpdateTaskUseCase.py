from ManageTasks.domain.ports.taskport import TaskPort


class UpdateUseCase:
    def __init__(self, task_port: TaskPort):
        self.repository = task_port

    def run(self, id, name):
        self.repository.update_task(id, name)
