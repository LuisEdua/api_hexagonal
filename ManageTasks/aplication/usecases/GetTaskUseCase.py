from ManageTasks.domain.ports.taskport import TaskPort


class GetUseCase:
    def __init__(self, task_port: TaskPort):
        self.repository = task_port

    def run(self):
        return self.repository.get_tasks()
