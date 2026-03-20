from flask import Blueprint,request,jsonify
from model import *
PriceType_blueprint=Blueprint("PriceType_blueprint",__name__)

@PriceType_blueprint.route('/pricetype', methods=['POST'])
def pricetype():
    data = request.get_json()
    pricetype= PriceType(
        name=data.get('name'),
        description= data.get('description'),
        vendorId= data.get('vendorId'))

    db.session.add(pricetype)
    db.session.commit()

    return jsonify({"message": "Pricing created successfully"})


@PriceType_blueprint.route('/pricing', methods=['GET'])
def fetch_all_pricing():
    pricing_list = PriceType.query.all()
    return jsonify([PriceType.to_dict() for pricing in pricing_list])


@PriceType_blueprint.route('/pricing/<int:pricing_id>', methods=['GET'])
def fetch_pricing_by_id(pricing_id):
    pricing = PriceType.query.get(pricing_id)

    if not pricing:
        return jsonify({'message': 'Pricing not found'}), 404

    return jsonify(pricing.to_dict())


@PriceType_blueprint.route('/pricing/<int:pricing_id>', methods=['PUT'])
def update_pricing(pricing_id):
    pricing = PriceType.query.get(pricing_id)

    if not pricing:
        return jsonify({'message': 'Pricing not found'}), 404

    data = request.get_json()

    pricing.name = data.get('name', pricing.name)
    pricing.description = data.get('description', pricing.description)
    pricing.vendorId = data.get('vendorId', pricing.vendorId)
    db.session.commit()

    return jsonify({
        'message': 'Pricing updated successfully',
        'pricing': PriceType.to_dict()
    })


@PriceType_blueprint.route('/pricing/delete/<int:pricing_id>', methods=['PUT'])
def delete_pricing(pricing_id):
    pricing = PriceType.query.get(pricing_id)

    if not pricing:
        return jsonify({'message': 'Pricing not found'}), 404

    db.session.delete(pricing)
    db.session.commit()

    return jsonify({'message': 'Pricing deleted successfully'})

