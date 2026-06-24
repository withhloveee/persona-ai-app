from flask_sqlalchemy import SQLAlchemy
from main import app,db
from werkzeug.security import generate_password_hash

class Users(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    daily_token_limit = db.Column(db.Integer, nullable=False, default=20000)
    daily_tokens_used = db.Column(db.Integer, nullable=False, default=0)
    
with app.app_context():
    db.create_all()
    admin = Users(username="portal@admin",password=generate_password_hash("admin@02"))
    
    if not admin:
        db.session.add(admin)
        db.session.commit()