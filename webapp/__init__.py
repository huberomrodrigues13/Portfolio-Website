from flask import Flask

#If we need a database:
'''
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
DB_NAME = "database"
'''

app = Flask(__name__)
SECRET_KEY = "1234567890102938475629384756384756576574849302SECRETKEY"

def create_app():
    app.config["SECRET_KEY"] = SECRET_KEY

    from .routes import core
    app.register_blueprint(core)

    return app