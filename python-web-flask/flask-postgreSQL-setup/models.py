from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class User(db.Model):
    """Model for the users table"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255),nullable=False)
    birthday = db.Column(db.String(10))
    phone = db.Column(db.String(10), unique=True, nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)

