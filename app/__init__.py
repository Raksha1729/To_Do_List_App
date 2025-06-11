from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#create database object globally
db=SQLAlchemy()

def create_app(): # This creates a flask app
    app=Flask(__name__)

    app.config['SECRET_KEY']='your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI']='sqllite:///todo.db' #Database location
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    db.__init__(app) #db object linked to the specific app

    # register blueprints is the way to organize our application into modular components
    from app.routes.auth import auth_bp
    from app.routes.auth import tasks_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    return app