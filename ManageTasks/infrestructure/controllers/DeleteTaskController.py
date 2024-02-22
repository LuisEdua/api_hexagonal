from ManageTasks.aplication.usecases.DeleteTaskUseCase import DeleteUseCase
from ManageTasks.domain.ports.taskport import TaskPort
from ManageTasks.infrestructure.controllers.dtos.taskresponse import taskresponse_dto
from flask import jsonify


class DeleteTaskController:
    def __init__(self, task_port: TaskPort):
        self.use_case = DeleteUseCase(task_port)

    def run(self, id):
        self.use_case.run(id)
        return jsonify({'message': "Task deleted successfully"})
