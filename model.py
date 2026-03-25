from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
# -------- Users --------
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile_number = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=True)
    role = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    vendorId = db.Column(db.Integer)
    delete_status = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'mobileNumber': self.mobile_number,
            'password':self.password,
            'role': self.role,
            'status': self.status,
            'vendorId': self.vendorId
        }


# -------- Media --------
class MediaFiles(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    vendorId = db.Column(db.Integer)
    file_name = db.Column(db.String(200), nullable=False)
    file_url = db.Column(db.String(500), nullable=False)
    file_title = db.Column(db.String(100))
    file_type = db.Column(db.String(100), nullable=False)
    alt_text = db.Column(db.String(200))
    entity_type = db.Column(db.String(50), nullable=False)
    entity_id = db.Column(db.Integer, nullable=False)
    delete_status = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'vendor_id': self.vendorId,
            'file_name': self.file_name,
            'file_url': self.file_url,
            'file_title': self.file_title,
            'file_type': self.file_type,
            'alt_text': self.alt_text,
            'entity_type': self.entity_type,
            'entity_id': self.entity_id
        }
    

# -------- Product --------
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    parent_id = db.Column(db.Integer)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    price = db.Column(db.Float, nullable=False)
    sku_id = db.Column(db.String(100), unique=True, nullable=False)
    barcode = db.Column(db.String(100), unique=True)
    brand_id = db.Column(db.Integer)
    vendorId = db.Column(db.Integer, nullable=False)
    product_type = db.Column(db.String(50), nullable=False)
    def to_dict(self):
        return {
            'id': self.id,
            'parent_id': self.parent_id,
            'name': self.name,
            'description': self.description,
            'sku_id': self.sku_id,
            'barcode': self.barcode,
            'price': self.price,
            'vendor_id': self.vendorId,
            'brand_id': self.brand_id,
            'product_type': self.product_type
        }


# -------- Pricetype --------
class PriceType(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    vendorId = db.Column(db.Integer,nullable=False)
    
    def to_dict(self):
        __tablename__ = "price_type"
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'vendorId': self.vendorId
            }

# -------- Currency --------
class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Float, nullable=False)
    charges = db.Column(db.Float)
    def to_dict(self):
        return {
            'id': self.id,
            'code': self.code,
            'name': self.name,
            'value': self.value,
            'charges': self.charges
        }
