from ManageTasks.infrestructure.repositories.repository import Repository
from ManageTasks.infrestructure.controllers.CreateTaskController import CreateTaskController
from ManageTasks.infrestructure.controllers.GetTaskController import GetTaskController
from ManageTasks.infrestructure.controllers.UpdateTaskController import UpdateTaskController
from ManageTasks.infrestructure.controllers.DeleteTaskController import DeleteTaskController
from flask import Blueprint, request


repository = Repository()
create_case = CreateTaskController(repository)
get_case = GetTaskController(repository)
update_case = UpdateTaskController(repository)
delete_case = DeleteTaskController(repository)

task_routes = Blueprint('task_routes', __name__)

@task_routes.route('/', methods=['GET'])
def get():
    return get_case.run()

@task_routes.route('/', methods=['POST'])
def create():
    return create_case.run(request)

@task_routes.route('/string:id/string:name', methods=['PUT'])
def update(id, name):
    return update_case.run(id, name)

@task_routes.route('/string:id', methods=['DELETE'])
def delete(id):
    return delete_case.run(id)