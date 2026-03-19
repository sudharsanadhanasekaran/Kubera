from flask import Blueprint, request, jsonify
from models import db, Users

user_bp = Blueprint("user_bp", __name__)

# CREATE
@user_bp.route("/", methods=["POST"])
def create_user():
    data = request.json 

    user = Users(
        name=data["name"],
        email=data["email"],
        mobile_number=data.get("mobile_number"),
        password=data["password"],
        role=data["role"],
        status=data["status"]
    )

    db.session.add(user)
    db.session.commit()

    return "User created successfully", 201

# READ
@user_bp.route("/", methods=["GET"])
def get_users():
    users = Users.query.filter_by(is_deleted=False).all()
    return jsonify([u.to_dict() for u in users])

# UPDATE
@user_bp.route("/<int:id>", methods=["PUT"])
def update_user(id):
    user = Users.query.get(id)

    if not user or user.is_deleted:
        return {"msg": "User not found"}

    data = request.json
    user.name = data.get("name", user.name)
    user.role = data.get("role", user.role)
    user.status = data.get("status", user.status)
    user.email = data.get("email", user.email)
    user.mobile_number = data.get("mobile_number", user.mobile_number)
    user.password = data.get("password", user.password)

    db.session.commit()
    return "User updated successfully"

# SOFT DELETE
@user_bp.route("/<int:user_id>/delete", methods=["PUT"])
def soft_delete_user(user_id):
    user = Users.query.get(user_id)

    if not user or user.is_deleted:
        return {"msg": "User not found or already deleted"}

    user.is_deleted = True
    db.session.commit()

    return {"msg": "User soft deleted successfully"}