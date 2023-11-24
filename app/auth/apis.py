from core.user.constants import UserRole
from flask import Blueprint, request
from marshmallow import Schema, fields, ValidationError, validate, validates
from core.auth.services import AuthService
from app.depedency_injection import injector

auth_blueprint = Blueprint('auth', __name__)
auth_service = injector.get(AuthService)

class UserRegistrationSchema(Schema):
    username = fields.String(required=True, validate=validate.Length(min=3))
    password = fields.String(required=True, validate=validate.Length(min=5), load_only=True)
    bio = fields.String(required=False, validate=validate.Length(max=255))
    role = fields.Enum(UserRole, required=True)

@auth_blueprint.route("/registration", methods=["POST"])
def register():
    data = request.get_json()
    schema = UserRegistrationSchema()
    try:
        data = schema.load(data)
    except ValidationError as err:
        return {"error": err.messages}, 400
    
    return schema.dump(auth_service.register(
        data['username'], data['password'], data['bio'], data['role']
    ))


class UserLoginSchema(Schema):
    username = fields.String(required=True, validate=validate.Length(min=3))
    password = fields.String(required=True, validate=validate.Length(min=5), load_only=True)


@auth_blueprint.route("/login", methods=["POST"])
def login():
    schema = UserLoginSchema()
    try:
        data = schema.load(request.get_json())
    except ValidationError as err:
        return {"error": err.messages}, 400
    
    result = auth_service.login(
        username=data['username'],
        password=data['password']
    )

    if not result:
        return {"error": "User or password is not valid"}, 401
    
    return result
