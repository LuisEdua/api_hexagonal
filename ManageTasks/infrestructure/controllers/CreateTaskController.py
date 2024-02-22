from ManageTasks.aplication.usecases.CreateTaskUseCase import CreateUseCase
from ManageTasks.domain.ports.taskport import TaskPort
from ManageTasks.infrestructure.controllers.dtos.taskresponse import taskresponse_dto
from flask import jsonify


class CreateTaskController:
    def __init__(self, repository: TaskPort):
        self.use_ase = CreateUseCase(repository)

    def run(self, request):
        return jsonify(taskresponse_dto(self.use_ase.run(request.get_json())))
