from flask_sqlalchemy import SQLAlchemy
import os

def init_db(app):
    db = SQLAlchemy(app)
    return db  