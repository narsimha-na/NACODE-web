import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

##Getting the file path from the OS Library
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

##Intilizing the SQL diretory to the App
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

###########################################

class Puppy(db.Model):

    #Manually assigning the table name to Database
    __tablename__ = 'na'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr(self):
        return f"Puppy {self.name} is {self.age} years old "
