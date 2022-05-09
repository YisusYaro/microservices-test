import os

import flask
from waitress import serve

from app_controller import app_controller
from shared.infraestructure.dependency_injection.app import App
from comics.interface.controller import comics_controller

app = flask.Flask(__name__)


def main():
    env = os.environ.get("ENV")
    App().set_comics_module()

    app.register_blueprint(app_controller)
    app.register_blueprint(comics_controller)

    if(env == "production"):
        serve(app, host="0.0.0.0", port=5002)
        return

    app.debug = True
    app.run(host='0.0.0.0', port=5002)


if __name__ == "__main__":
    main()
