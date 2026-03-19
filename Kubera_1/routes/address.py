from flask import Blueprint, request, jsonify
from models import db, Address

address_bp = Blueprint("address_bp", __name__)

# CREATE (POST)
@address_bp.route("/", methods=["POST"])
def create_address():
    data = request.get_json()

    address = Address(
        user_id=data.get("user_id"),
        vendor_id=data.get("vendor_id"),
        address_line1=data.get("address_line1"),
        city=data.get("city"),
        state=data.get("state"),
        postal_code=data.get("postal_code"),
        country=data.get("country")
    )

    db.session.add(address)
    db.session.commit()

    return jsonify({
        "msg": "Address created successfully",
        "data": address.to_dict()
    }), 201


# READ ALL (GET)
@address_bp.route("/", methods=["GET"])
def get_addresses():
    addresses = Address.query.filter_by(is_deleted=False).all()

    return jsonify({
        "msg": "Addresses fetched successfully",
        "data": [a.to_dict() for a in addresses]
    }), 200


# READ SINGLE (GET)
@address_bp.route("/<int:id>", methods=["GET"])
def get_address(id):
    address = Address.query.get(id)

    if not address or address.is_deleted:
        return jsonify({"msg": "Address not found"}), 404

    return jsonify({
        "msg": "Address fetched successfully",
        "data": address.to_dict()
    }), 200


# UPDATE (PUT)
@address_bp.route("/<int:id>", methods=["PUT"])
def update_address(id):
    address = Address.query.get(id)

    if not address or address.is_deleted:
        return jsonify({"msg": "Address not found"}), 404

    data = request.get_json()

    address.user_id = data.get("user_id", address.user_id)
    address.vendor_id = data.get("vendor_id", address.vendor_id)
    address.address_line1 = data.get("address_line1", address.address_line1)
    address.city = data.get("city", address.city)
    address.state = data.get("state", address.state)
    address.postal_code = data.get("postal_code", address.postal_code)
    address.country = data.get("country", address.country)

    db.session.commit()

    return jsonify({
        "msg": "Address updated successfully",
        "data": address.to_dict()
    }), 200


# SOFT DELETE (PUT)
@address_bp.route("/<int:id>/delete", methods=["PUT"])
def soft_delete_address(id):
    address = Address.query.get(id)

    if not address or address.is_deleted:
        return jsonify({"msg": "Address not found or already deleted"}), 404

    address.is_deleted = True
    db.session.commit()

    return jsonify({
        "msg": "Address soft deleted successfully"
    }), 200