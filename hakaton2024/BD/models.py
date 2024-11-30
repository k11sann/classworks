from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'QWERTYUIOP'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///hac.db'

db = SQLAlchemy(app)

class Auth(db.Model):
    __tablename__ = 'auth'
    id = db.Column(db.Integer(), primary_key=True)
    login = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)

class User(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer(), primary_key=True)
    id_auth = db.Column(db.Integer(), nullable=False)

class Problem(db.Model):
    __tablename__ = 'problem'
    id = db.Column(db.Integer(), primary_key=True)
    id_user = db.Column(db.Integer(), nullable=False)
    id_text_problem = db.Column(db.Integer())
    id_type_problem = db.Column(db.Integer())
    date_problem = db.Column(db.DateTime(), default=datetime.utcnow)
    views_problem = db.Column(db.Integer())
    id_comments_problem = db.Column(db.Integer())

class Text_problem(db.Model):
    __tablename__ = 'text_problem'
    id = db.Column(db.Integer(), primary_key=True)
    problemText = db.Column(db.String(255))

class Type_problem(db.Model):
    __tablename__ = 'type_problem'
    id = db.Column(db.Integer(), primary_key=True)
    problemType = db.Column(db.String(255))

class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer(), primary_key=True)
    id_type_comments = db.Column(db.Integer())

class Type_comments(db.Model):
    __tablename__ = 'type_comments'
    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.String(255))

db.create_all()
