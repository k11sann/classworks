from sqlalchemy import *
from flask_sqlalchemy import SQLAlchemy

#from flask import Flask
#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prt.db'
#db = SQLAlchemy(app)

db = SQLAlchemy

class Auth(db.Model):
    __tablename__ = 'auth'
    auth_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    auth_login = db.Column(db.String(25), unique=True, nullable=False)
    auth_password = db.Column(db.String(50), nullable=False)
    auth_email = db.Column(db.String(255))
    
class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_url_image = db.Column(db.String(25), unique=True, nullable=False)
    user_firstname = db.Column(db.String(50), nullable=False)
    user_bdate = db.Column(Date, nullable=False)
    user_country = db.Column(db.String(100))
    user_id_education = db.Column(db.Integer)
    user_comment = db.Column(db.String(255))
    user_id_auth = db.Column(db.Integer)    
    
class Education(db.Model):
    __tablename__ = 'education'
    education_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    education_name = db.Column(db.String(255))   
    
class Skills(db.Model):
    __tablename__ = 'skills'
    skills_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    skills_id_user = db.Column(db.Integer)    
    skills_id_type = db.Column(db.Integer)
    
class Type_skills(db.Model):
    __tablename__ = 'type_skills'
    type_skills_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_skills_name = db.Column(db.String(255))    
    
class Socials(db.Model):
    __tablename__ = 'socials'
    socials_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    socials_id_user = db.Column(db.Integer, nullable=False)    
    socials_id_type_socials = db.Column(db.Integer)
    
class Type_socials(db.Model):
    __tablename__ = 'type_socials'
    type_socials_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_socials_name = db.Column(db.String(255))       
    type_socials_url = db.Column(db.String(255))    
    
#with app.app_context():
#    db.create_all()
#    db.session.commit()