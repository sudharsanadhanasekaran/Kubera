from flask import Blueprint,request,jsonify
from model import *
from datetime import datetime
currency_blueprint=Blueprint("currency_blueprint",__name__)

@currency_blueprint.route('/currency',methods=['GET'])
def get_all_currency():
        get_currency=Currency.query.all()
        result = []
        for currency in get_currency:
            result.append(currency.to_dict())
        return jsonify(result)   
    
@currency_blueprint.route('/currency', methods=['POST'])
def new_currency():
    data = request.get_json()
    new_currency = Currency(
        code=data.get("code"),
        name=data.get("name"),
        value=data.get("value"),
        charges=data.get("charges")
    )

    db.session.add(new_currency)
    db.session.commit()

    # if not currency or currency.delete_status:
    #     return jsonify({"message": "Currency not found"}), 404  

@currency_blueprint.route('/currency/<int:id>',methods=['PUT'])
def update_currency(id):
    data = request.get_json()
    currency = Currency.query.get(id)
    if not currency or currency.delete_status:
        return jsonify({"message": "User not found"})
    
    currency.code  = data.get("code",currency.code)
    currency.name = data.get("name", currency.name)
    currency.value = data.get("value",currency.value)
    currency.charges=data.get("password",currency.charges)
  
    db.session.commit()

    return jsonify({
        "message": "User updated successfully",
        "user": currency.to_dict()
    })                           
@currency_blueprint.route('/currency/<int:id>', methods=['DELETE'])
def soft_delete_currency(id):
    currency = Currency.query.get(id)

    # if not currency or currency.delete_status:
    #     return jsonify({"message": "Currency not found"}), 404

    currency.delete_status = True
    currency.deleted_at = datetime.utcnow()

    db.session.commit()

    return jsonify({"message": "Currency soft deleted successfully"})