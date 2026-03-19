from flask import Flask
from models import db

from routes.user import user_bp
from routes.vendor import vendor_bp
from routes.address import address_bp
from routes.product_price import price_bp
from routes.language import language_bp
from sqlalchemy import event



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Sql2026@localhost/Ecommerce'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def home():
    return "Welcome to the E-commerce API"

# Register Blueprints
app.register_blueprint(user_bp, url_prefix="/users")
app.register_blueprint(vendor_bp, url_prefix="/vendors")
app.register_blueprint(address_bp, url_prefix="/address")
app.register_blueprint(price_bp, url_prefix="/price")
app.register_blueprint(language_bp, url_prefix="/language")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, port=8000)