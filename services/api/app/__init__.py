from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()

app = Flask(__name__)
app.config.from_object("app.config.Config")

db.init_app(app)
ma.init_app(app)

# setup routes
from app.resources.routes import initialize_routes
initialize_routes(app)

