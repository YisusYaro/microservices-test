import os

import flask
from waitress import serve

from app_controller import app_controller
from resources.interface.controller import resources_controller
from resources.infraestructure.dependency_injection.resources_module import setResourcesModule
from shared.infraestructure.dependency_injection.app import App

app = flask.Flask(__name__)


def main():
    env = os.environ.get("ENV")

    App()
    setResourcesModule()

    app.register_blueprint(app_controller)
    app.register_blueprint(resources_controller)

    if(env == "production"):
        serve(app, host="0.0.0.0", port=5000)
        return

    app.debug = True
    app.run(host='0.0.0.0', port=5000)


if __name__ == "__main__":
    main()
