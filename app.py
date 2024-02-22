from flask import Flask
from ManageTasks.infrestructure.routes.TaskRoutes import task_routes

app = Flask(__name__)


app.register_blueprint(task_routes, url_prefix="/task")


if __name__ == '__main__':
    app.run()
