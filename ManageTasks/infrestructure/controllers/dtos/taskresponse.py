def taskresponse_dto(task):
    return {"id": task.id, "name": task.name, "description": task.description, "status": task.status}
