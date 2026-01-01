from flask import Flask
from decouple import config
from app.database import db, migrate
from app.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # from app.routes import main_router
    # app.register_blueprint(main_router)

    return app