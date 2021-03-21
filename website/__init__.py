from flask import Flask

def create_app():
    #name of the file initialize flask
    app = Flask(__name__)
    # encrypt session data, cookies etc, in production dont share secrete key
    app.config['SECRET_KEY'] = '123456789' 
     
    # register views/routes
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
