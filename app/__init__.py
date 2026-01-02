from flask import Flask, g
from flask_login import LoginManager, current_user, login_manager
from app.models import User
from app.database import db, migrate
from app.config import Config
from app import models
from app.context_process import FlaskStyleUser
from app.routers.v1 import main_router, auth_router


# global login_manager
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # intial flask login
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message = 'لطفاً برای دسترسی به این صفحه وارد شوید'
    login_manager.login_message_category = 'warning'

    # Register blueprints
    app.register_blueprint(main_router)
    app.register_blueprint(auth_router, url_prefix="/auth")

    # context process
    @app.context_processor
    def inject_user():
        flask_user = FlaskStyleUser(current_user)
        return {
            "user": flask_user,
            "request": g
        }
    
    @app.before_request
    def load_user_to_g():
        g.user = current_user

    return app