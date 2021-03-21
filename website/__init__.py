from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    #name of the file initialize flask
    app = Flask(__name__)
    # encrypt session data, cookies etc, in production dont share secrete key
    app.config['SECRET_KEY'] = '123456789' 
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' 
    db.init_app(app)
    
    # register views/routes
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
