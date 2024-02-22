import uuid

class Tasks:
    def __init__(self, name, description, status):
        self.uuid = uuid.uuid4()
        self.name = name
        self.description = description
        self.status = status
