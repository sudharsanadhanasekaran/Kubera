from flask import Blueprint,request,jsonify
from model import *
Product_blueprint=Blueprint("Product_blueprint",__name__)
@Product_blueprint.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(
        parent_id=data.get('parent_id'),
        name=data['name'],
        description=data.get('description'),
        price=data['price'],
        sku_id=data['sku_id'],
        barcode=data.get('barcode'),
        brand_id=data.get('brand_id'),
        vendorId=data.get('vendorId'),
        product_type=data['product_type'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({
            "message": "Product created successfully",
            "product": new_product.to_dict() }), 201
@Product_blueprint.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([Product.to_dict() for Product in products])
#--get product by id
@Product_blueprint.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(Product.to_dict())
#---update product
@Product_blueprint.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    product.parent_id = data.get('parent_id', product.parent_id)
    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.sku_id = data.get('sku_id', product.sku_id)
    product.barcode = data.get('barcode', product.barcode)
    product.brand_id = data.get('brand_id', product.brand_id)
    product.vendorId = data.get('vendorId', product.vendorId)
    product.product_type = data.get('product_type', product.product_type)
    db.session.commit()
    return jsonify({
        "message": "Product updated successfully",
        "product": product.to_dict()})
#---soft delete product    
@Product_blueprint.route('/products/<int:id>', methods=['PUT'])
def delete_product(id):
    product = Product.query.get_or_404(id)

    db.session.delete(product)
    db.session.commit()

    return jsonify({
        "message": "Product deleted successfully"})
    
    '''
    "parent_id":6,
    "name": "pri",
    "description": "home appliance",
    "price": 902,
    "sku_id":600,
    "barcode": "959523",
    "brand_id": 900,
    "vendorId": 78,
    "product_type": "grinder"
}'''