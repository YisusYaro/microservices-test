from flask import Blueprint

app_controller = Blueprint('app_controller', __name__)


@app_controller.route("/")
def health_check():
    return "Server is working. ✨"
