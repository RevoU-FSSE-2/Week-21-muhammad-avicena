from flask import Blueprint

home_blueprint = Blueprint("home_blueprint", __name__)

@home_blueprint.route("", methods=["GET"])
def home_routes():
    return {"message" : "Hello World !"}, 200