from dotenv import load_dotenv
load_dotenv()

from flask import Flask, jsonify
app = Flask(__name__)
app.config.from_object('settings.app_config')

from database import init_db
db = init_db(app)

from flask_marshmallow import Marshmallow
ma = Marshmallow(app)

from commands import db_commands
app.register_blueprint(db_commands)

from controllers import registerable_controllers

for controller in registerable_controllers:
    app.register_blueprint(controller)

from marshmallow.exceptions import ValidationError

@app.errorhandler(ValidationError)
def handle_bad_request(error):
    return (jsonify(error.messages), 400)