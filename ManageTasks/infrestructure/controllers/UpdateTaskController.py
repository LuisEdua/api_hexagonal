from ManageTasks.aplication.usecases.UpdateTaskUseCase import UpdateUseCase
from ManageTasks.domain.ports.taskport import TaskPort
from ManageTasks.infrestructure.controllers.dtos.taskresponse import taskresponse_dto
from flask import jsonify


class UpdateTaskController:
    def __init__(self, task_port: TaskPort):
        self.use_case = UpdateUseCase(task_port)

    def run(self, id:str, task_name:str):
        return jsonify(taskresponse_dto(self.use_case.run(id, task_name)))
