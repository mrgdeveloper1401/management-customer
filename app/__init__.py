from flask import Flask
from app.database import db, migrate
from app.config import Config
# Import models so Alembic can discover them
from app import models


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # from app.routes import main_router
    # app.register_blueprint(main_router)

    return app