from flask import Blueprint, request, jsonify
from models import db, Language

language_bp = Blueprint("language_bp", __name__)

# CREATE
@language_bp.route("/", methods=["POST"])
def create_language():
    data = request.json

    lang = Language(
        name=data["name"],
        code=data["code"],
        vendor_id=data["vendor_id"]
    )

    db.session.add(lang)
    db.session.commit()

    return jsonify({
        "msg": "Language created successfully",
        "data": lang.to_dict()
    })


# READ
@language_bp.route("/", methods=["GET"])
def get_languages():
    languages = Language.query.filter_by(is_deleted=False).all()

    return jsonify({
        "msg": "Languages fetched successfully",
        "data": [l.to_dict() for l in languages]
    })


# UPDATE
@language_bp.route("/<int:id>", methods=["PUT"])
def update_language(id):
    lang = Language.query.get(id)

    if not lang or lang.is_deleted:
        return jsonify({"msg": "Language not found"}), 404

    data = request.json

    lang.name = data.get("name", lang.name)
    lang.code = data.get("code", lang.code)
    lang.vendor_id = data.get("vendor_id", lang.vendor_id)

    db.session.commit()

    return jsonify({
        "msg": "Language updated successfully",
        "data": lang.to_dict()
    })


# SOFT DELETE (PUT)
@language_bp.route("/<int:id>/delete", methods=["PUT"])
def soft_delete_language(id):
    lang = Language.query.get(id)

    if not lang or lang.is_deleted:
        return jsonify({"msg": "Language not found or already deleted"}), 404

    lang.is_deleted = True
    db.session.commit()

    return jsonify({
        "msg": "Language soft deleted successfully"
    })