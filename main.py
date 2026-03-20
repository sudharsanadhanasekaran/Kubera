from flask import Flask, jsonify, request
from routes.Users import Users_blueprint
from routes.PriceType import PriceType_blueprint
from routes.MediaFiles import MediaFiles_blueprint
from routes.product import Product_blueprint
from routes.currency import currency_blueprint
from sqlalchemy import text
from model import *
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:Kalandharun8@localhost/E_com"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.sort_keys = False

init_db(app)

@app.route('/')
def home():
    return "Flask API Running"

app.register_blueprint(currency_blueprint)

app.register_blueprint(MediaFiles_blueprint)

app.register_blueprint(PriceType_blueprint)

app.register_blueprint(Product_blueprint)

app.register_blueprint(Users_blueprint)

if __name__=="__main__":
    app.run(debug=True)
    