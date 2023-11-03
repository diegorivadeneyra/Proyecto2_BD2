# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime 


database_path='postgresql://postgres:1@localhost:5432/BD2'

#Configuracion
db=SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI']=database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    db.app=app
    db.init_app(app)
    with app.app_context():
        db.create_all()

#Modelos para la BD-fashion
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key = True)
    gender = db.Column(db.Text,nullable = False)
    masterCategory = db.Column(db.Text,nullable = False)
    subCategory = db.Column(db.Text, nullable = False)
    articleType = db.Column(db.Text,nullable = False)
    baseColour = db.Column(db.Text,nullable = False)
    season = db.Column(db.Text,nullable = False)
    year = db.Column(db.Integer,nullable = False)
    usage = db.Column(db.Text,nullable = False)

    def format(self):
        return {
            'id':self.id,
            'gender':self.gender,
            'masterCategory':self.masterCategory,
            'subCategory':self.subCategory,
            'articleType':self.articleType,
            'baseColour':self.baseColour,
            'season':self.season,
            'year':self.year,
            'usage':self.usage
        }

    #Metodo que permite la inserción de un post a través de nuestra API
    def insert(self):
        db.session.add(self)
        db.session.commit()

    #Metodo para la actualizazcion de un post a través de nuestra API
    def update(self):
        db.session.commit()

    #Metodo para la eliminacion de un post a través de nuestra API
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Query(db.Model):
    __tablename__ = 'query'
    id = db.Column(db.Integer, primary_key = True)
    stopwords = db.Column(db.Text)
    
    #Metodo que formatee el objeto a json para devolverlo a mi API y que no de errores
    def format(self):
        return {
            'id':self.id,
            'stopword':self.stopwords,
        }

    #Metodo para la inserción de un post a través de nuestra API
    def insert(self):
        db.session.add(self)
        db.session.commit()

    #Metodo para la actualizazcion de un post a través de nuestra API
    def update(self):
        db.session.commit()

    #Metodo para la eliminacion de un post a través de nuestra API
    def delete(self):
        db.session.delete(self)
        db.session.commit()
