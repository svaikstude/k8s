import datetime

from flask import current_app
from sqlalchemy.sql import func

from project import db


class Book(db.Model):

    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    read = db.Column(db.Boolean(), default=False, nullable=False)

    def __init__(self, title, author, read):
        self.title = title
        self.author = author
        self.read = read

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'read': self.read
        }
        
        
class Table(db.Model):
    __tablename__ = 'tables'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    manufacturer = db.Column(db.String(20), nullable=False)
    model = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    photo = db.Column(db.String(500), nullable=False)
    
    
    def __init__(self, model, manufacturer, photo, price):
        self.manufacturer = manufacturer
        self.model = model
        self.photo = photo
        self.price = price
        
    def to_json(self):
        return {
            'model': self.model,
            'manufacturer': self.manufacturer,
            'photo': self.photo,
            'price': self.price
        }