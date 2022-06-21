from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

dataBase = SQLAlchemy()
dbName = "database.db"

def createApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Michael Uchiha'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{dbName}'
    dataBase.init_app(app)

    from .auth import auth
    from .views import views

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    createDatabase(app)

    loginManager = LoginManager()
    loginManager.login_view = 'auth.login'
    loginManager.init_app(app)

    @loginManager.user_loader
    def loadUser(id):
        return User.query.get(int(id))

    return app

def createDatabase(app):
    if not path.exists('website/' + dbName):
        dataBase.create_all(app=app)
        print('Database created.')