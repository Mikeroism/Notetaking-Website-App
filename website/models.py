from flask_login import UserMixin
from website import dataBase
from sqlalchemy.sql import func

class Note(dataBase.Model):
    id = dataBase.Column(dataBase.Integer, primary_key=True)
    data = dataBase.Column(dataBase.String(10000))
    date = dataBase.Column(dataBase.DateTime(timezone=True), default = func.now())
    userId = dataBase.Column(dataBase.Integer, dataBase.ForeignKey('user.id'))

class User(dataBase.Model, UserMixin):
    id = dataBase.Column(dataBase.Integer, primary_key = True )
    email = dataBase.Column(dataBase.String(150), unique = True)
    password = dataBase.Column(dataBase.String(150))
    firstName = dataBase.Column(dataBase.String(150))
    notes = dataBase.relationship('Note')