from flask import Flask
import os

#If we need a database:
'''
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
DB_NAME = "database"
'''

app = Flask(__name__)
SECRET_KEY = os.getenv("SECRET_KEY", "fallback_secret_key")

def create_app():
    app.config["SECRET_KEY"] = SECRET_KEY

    from .routes import core
    app.register_blueprint(core)

    return app