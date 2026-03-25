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
    print("message:Pricing created successfully",pricetype.to_dict())
    return jsonify(pricetype.to_dict())


@PriceType_blueprint.route('/pricetype', methods=['GET'])
def get_pricing():
    pricing_list=PriceType.query.all()
    result = []
    for pricing in pricing_list:
        result.append(pricing.to_dict())
    return jsonify(result)

@PriceType_blueprint.route('/pricetype/<int:id>', methods=['GET'])
def fetch_pricing_by_id(id):
    pricing = PriceType.query.get(id)

    if not pricing:
        return jsonify({'message': 'Pricing not found'}), 404

    return jsonify(pricing.to_dict())


@PriceType_blueprint.route('/pricetype/<int:id>', methods=['PUT'])
def update_pricing(id):
    pricing = PriceType.query.get(id)

    if not pricing:
        return jsonify({'message': 'Pricing not found'}), 404

    data = request.get_json()

    pricing.name = data.get('name', pricing.name)
    pricing.description = data.get('description', pricing.description)
    pricing.vendorId = data.get('vendorId', pricing.vendorId)
    db.session.commit()

    return jsonify({
        'message': 'Pricing updated successfully',
        'pricing': pricing.to_dict()
    })


@PriceType_blueprint.route('/pricetype/delete/<int:id>', methods=['PUT'])
def delete_pricing(id):
    pricing = PriceType.query.get(id)

    if not pricing:
        return jsonify({'message': 'Pricing not found'}), 404

    db.session.delete(pricing)
    db.session.commit()

    return jsonify({'message': 'Pricing deleted successfully'})

