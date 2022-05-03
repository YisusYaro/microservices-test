import os
import flask
from waitress import serve
from app_controller import app_controller

app = flask.Flask(__name__)

def main():
    env = os.environ.get("ENV")

    app.register_blueprint(app_controller)

    if(env=="production"):
        serve(app, host="0.0.0.0", port=5000)
        return

    app.debug = True
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()
