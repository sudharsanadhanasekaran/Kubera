from flask import Blueprint, request, jsonify
from models import db, Vendors

vendor_bp = Blueprint("vendor_bp", __name__)

# CREATE (POST)
@vendor_bp.route("/", methods=["POST"])
def create_vendor():
    data = request.get_json()

    vendor = Vendors(
        business_name=data.get("business_name"),
        email=data.get("email"),
        mobile_number=data.get("mobile_number"),
        address_id=data.get("address_id")
    )

    db.session.add(vendor)
    db.session.commit()

    return jsonify({
        "msg": "Vendor created successfully",
        "data": vendor.to_dict()
    }), 201


# READ (GET)
@vendor_bp.route("/", methods=["GET"])
def get_vendors():
    vendors = Vendors.query.filter_by(is_deleted=False).all()

    return jsonify({
        "msg": "Vendors fetched successfully",
        "data": [v.to_dict() for v in vendors]
    }), 200


# UPDATE (PUT)
@vendor_bp.route("/<int:id>", methods=["PUT"])
def update_vendor(id):
    vendor = Vendors.query.get(id)

    if not vendor or vendor.is_deleted:
        return jsonify({"msg": "Vendor not found"}), 404

    data = request.get_json()

    vendor.business_name = data.get("business_name", vendor.business_name)
    vendor.email = data.get("email", vendor.email)
    vendor.mobile_number = data.get("mobile_number", vendor.mobile_number)
    vendor.address_id = data.get("address_id", vendor.address_id)

    db.session.commit()

    return jsonify({
        "msg": "Vendor updated successfully",
        "data": vendor.to_dict()
    }), 200


# SOFT DELETE (PUT)
@vendor_bp.route("/<int:id>/delete", methods=["PUT"])
def soft_delete_vendor(id):
    vendor = Vendors.query.get(id)

    if not vendor or vendor.is_deleted:
        return jsonify({"msg": "Vendor not found or already deleted"}), 404

    vendor.is_deleted = True
    db.session.commit()

    return jsonify({
        "msg": "Vendor soft deleted successfully"
    }), 200