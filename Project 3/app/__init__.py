from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from config import Config

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()  # Khởi tạo bcrypt


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)  # Đăng ký bcrypt với Flask app

    # Import and register blueprints
    from app.controllers import bp as student_bp
    from app.auth import bp as auth_bp
    app.register_blueprint(student_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app