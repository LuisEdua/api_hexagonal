from ManageTasks.aplication.usecases.GetTaskUseCase import GetUseCase
from ManageTasks.domain.ports.taskport import TaskPort
from ManageTasks.infrestructure.controllers.dtos.taskresponse import taskresponse_dto
from flask import jsonify


class GetTaskController:
    def __init__(self, task_port: TaskPort):
        self.use_case = GetUseCase(task_port)

    def run(self):
        return jsonify({'data': [taskresponse_dto(task) for task in self.use_case.run()]})
