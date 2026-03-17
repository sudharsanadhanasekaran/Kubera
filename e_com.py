from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Tharani2704@localhost/ecom"

db=SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50))
    mobile_no = db.Column(db.String(10))
    email = db.Column(db.String(50),unique = True)
    password = db.Column(db.String(50))
    role = db.Column(db.String(50))
    status = db.Column(db.String(50))
    
    def to_dict(self):
        return{
            "id":self.id,
            "Name":self.name,
            "mobile_no":self.mobile_no,
            "email":self.email,
            "password":self.password,
            "role":self.role,
            "status":self.status
        }
@app.route("/home",methods=["Post"])
def create_user():
    data = request.json
    
    users = User(
        id=data["id"],
        name = data["name"],
        mobile_no = data["mobile_no"],
        email = data["email"],
        password = data["password"],
        role = data["role"],
        status = data["status"]
    )
    return jsonify({
        "messages":"create user succefully"
    })
    db.session.add(users)
    db.session.commit()
app.run(debug=True)

@app.route('/get',methods=["GET"])
def get():
    use = User.query.filter.all()
     