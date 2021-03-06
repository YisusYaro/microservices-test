import os

import flask
from waitress import serve

from app_controller import app_controller
from shared.infrastructure.dependency_injection.app import App
from users.interface.controller import users_controller

app = flask.Flask(__name__)


def main():
    env = os.environ.get("ENV")
    App().set_users_module()

    app.register_blueprint(app_controller)
    app.register_blueprint(users_controller)

    if(env == "production"):
        serve(app, host="0.0.0.0", port=5000)
        return

    app.debug = True
    app.run(host='0.0.0.0', port=5000)


if __name__ == "__main__":
    main()
