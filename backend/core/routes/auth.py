from main import app,db
from core.db import Users
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

@app.route('/register',methods=["POST"])
def register():
    username = request.json.get("username")
    password = request.json.get("password")
    
    user = Users(username=username,password=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    
    return {
        "message": "Registration successful",
        "username": user.username
    }, 201

@app.route('/login',methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    
    user = Users.query.filter_by(username=username).first()
    
    if not user:
        return {
            "message": "User not found"
        }, 404
    
    if check_password_hash(user.password,password):
        token = create_access_token(identity=str(user.id))
        return {
            "message": "Login successful",
            "token": token,
            "username": user.username
        }, 200
    else:
       return {
            "message": "Invalid credentials"
        }, 401