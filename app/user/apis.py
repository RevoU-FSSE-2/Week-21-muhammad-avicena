from flask import Blueprint
from app.auth.utils import user_required
from core.user.services import UserService
from app.depedency_injection import injector

user_service = injector.get(UserService)

user_blueprint = Blueprint("user_blueprint", __name__)

@user_blueprint.route("", methods=["GET"])
@user_required
def get_user(user_id):
    user = user_service.get_by_id(user_id=user_id)
    if not user:
        return {"error": "User not found"}, 404
    
    return {
        'id': user.id,
        'username': user.username,
        'role': user.role.value
    }
    

