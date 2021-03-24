from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from .api import AppApi

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    #name of the file initialize flask
    app = Flask(__name__)
    app_api = AppApi(app)
    # encrypt session data, cookies etc, in production dont share secrete key
    app.config['SECRET_KEY'] = '123456789' 
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' 
    db.init_app(app)

    # register views/routes
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    # app.register_blueprint(app_api.api_prefix, url_prefix='/api')

    from .models import User, Note
    create_database(app)

    # telling flask how to load a user
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Database Created!')




