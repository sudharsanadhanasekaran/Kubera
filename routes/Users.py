from flask import Blueprint,request,jsonify
from model import db, Users
Users_blueprint=Blueprint("Users_blueprint",__name__)
@Users_blueprint.route('/')
def home():
    return "Flask API Running"
# -------- create user --------
@Users_blueprint.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user =Users(
        name=data["name"],
        email=data["email"],
        mobile_number=data["mobile_number"],
        password=data["password"],
        role=data["role"],
        status=data["status"],
        vendorId=data["vendorId"]
    )
    db.session.add(new_user)
    db.session.commit()
    print("Saved user:", new_user.to_dict()) 
    return jsonify(new_user.to_dict())
# -------- get all users--------
@Users_blueprint.route("/users", methods=["GET"])
def get_users():
    users = Users.query.filter_by(delete_status=False).all()
    result = []
    for user in users:
        result.append(user.to_dict())
    return jsonify(result)
# --------get userby id--------
@Users_blueprint.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    user = Users.query.get(id)
    if not user or user.delete_status:
        return jsonify({"message": "User not found"})
    return jsonify(user.to_dict())
# --------update user--------#
@Users_blueprint.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    data = request.get_json()
    user = Users.query.get(id)
    if not user or user.delete_status:
        return jsonify({"message": "User not found"})
    
    user.name = data.get("name",user.name)
    user.email = data.get("email", user.email)
    user.mobile_number = data.get("mobile_number",user.mobile_number)
    user.password=data.get("password",user.password)
    user.role = data.get("role",user.role)
    user.status = data.get("status",user.status)
    user.vendorId=data.get("vendorId",user.vendorId)
    db.session.commit()

    return jsonify({
        "message": "User updated successfully",
        "user": user.to_dict()
    })
#---------update user by status----#
@Users_blueprint.route("/users/<int:id>/status", methods=["GET","PUT"])
def update_user_status(id):
    user = Users.query.get(id)
    if not user or user.delete_status:
        return jsonify({"message": "User not found"})
    if request.method == "GET":
        return jsonify({
            "status": user.status
        })
    data = request.get_json()

    user.status = data["status"]
    db.session.commit()

    return jsonify({
        "message": "User status updated successfully",
        "user": user.to_dict()
    })
#-------- delete user --------
@Users_blueprint.route("/users/<int:id>/delete", methods=["PUT"])
def delete_user(id):

    user = Users.query.get(id)

    if not user or user.delete_status:
        return jsonify({"message": "User not found"}), 404

    user.delete_status = True

    db.session.commit()

    return jsonify({
        "message": "User deleted successfully",
        "delete_status": user.delete_status
    })