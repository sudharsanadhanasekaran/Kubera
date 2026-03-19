from flask import Blueprint, request, jsonify
from models import db, ProductPrice

price_bp = Blueprint("price_bp", __name__)

# CREATE (POST)
@price_bp.route("/", methods=["POST"])
def create_price():
    data = request.get_json()

    price = ProductPrice(
        product_id=data.get("product_id"),
        price_type_id=data.get("price_type_id"),
        price=data.get("price"),
        currency_id=data.get("currency_id")
    )

    db.session.add(price)
    db.session.commit()

    return jsonify({
        "msg": "Product price created successfully",
        "data": price.to_dict()
    }), 201


# READ ALL (GET)
@price_bp.route("/", methods=["GET"])
def get_prices():
    prices = ProductPrice.query.filter_by(is_deleted=False).all()

    return jsonify({
        "msg": "Prices fetched successfully",
        "data": [p.to_dict() for p in prices]
    }), 200


# READ SINGLE (GET)
@price_bp.route("/<int:id>", methods=["GET"])
def get_price(id):
    price = ProductPrice.query.get(id)

    if not price or price.is_deleted:
        return jsonify({"msg": "Price not found"}), 404

    return jsonify({
        "msg": "Price fetched successfully",
        "data": price.to_dict()
    }), 200


# UPDATE (PUT)
@price_bp.route("/<int:id>", methods=["PUT"])
def update_price(id):
    price = ProductPrice.query.get(id)

    if not price or price.is_deleted:
        return jsonify({"msg": "Price not found"}), 404

    data = request.get_json()

    price.product_id = data.get("product_id", price.product_id)
    price.price_type_id = data.get("price_type_id", price.price_type_id)
    price.price = data.get("price", price.price)
    price.currency_id = data.get("currency_id", price.currency_id)

    db.session.commit()

    return jsonify({
        "msg": "Product price updated successfully",
        "data": price.to_dict()
    }), 200


# SOFT DELETE (PUT)
@price_bp.route("/<int:id>/delete", methods=["PUT"])
def soft_delete_price(id):
    price = ProductPrice.query.get(id)

    if not price or price.is_deleted:
        return jsonify({"msg": "Price not found or already deleted"}), 404

    price.is_deleted = True
    db.session.commit()

    return jsonify({
        "msg": "Product price soft deleted successfully"
    }), 200