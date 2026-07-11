from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

# Instância do banco de dados
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    # Inicializa o SQLAlchemy
    db.init_app(app)

    # Importa os models para que o SQLAlchemy conheça as tabelas
    from app import models

    # Registra as rotas
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    return app