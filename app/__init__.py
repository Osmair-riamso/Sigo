from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    # Importa os models
    from app import models

    # Importa apenas os Blueprints que já existem
    from app.routes.main import main_bp
    from app.routes.operadoras import operadoras_bp
    from app.routes.cidades import cidades_bp
    from app.routes.circuitos import circuitos_bp
    from app.routes.usuarios import usuarios_bp

    # Registra os Blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(operadoras_bp)
    app.register_blueprint(cidades_bp)
    app.register_blueprint(circuitos_bp)
    app.register_blueprint(usuarios_bp)

    return app
