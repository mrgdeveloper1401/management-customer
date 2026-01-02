from flask import Flask, session
from app.models import User
from app.database import db, migrate
from app.config import Config
# Import models so Alembic can discover them
from app import models


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # add blueprints
    from app.routes import main_router
    app.register_blueprint(main_router)

    # add context processors
    @app.context_processor
    def inject_user():
        user = None
        if "user_id" in session:
            user = User.query.get(session["user_id"])
        return dict(user=user)

    return app