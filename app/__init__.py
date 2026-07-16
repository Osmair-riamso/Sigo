from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.errors import register_error_handlers
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()

login_manager.login_view = "auth.login"
login_manager.login_message = "Faça login para acessar esta página."
login_manager.login_message_category = "warning"


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    # Importa os models
    from app import models

    @login_manager.user_loader
    def load_user(user_id):
        return models.Usuario.query.get(int(user_id))

    # Importa os Blueprints
    from app.routes.main import main_bp
    from app.routes.operadoras import operadoras_bp
    from app.routes.cidades import cidades_bp
    from app.routes.circuitos import circuitos_bp
    from app.routes.usuarios import usuarios_bp
    from app.routes.auth import auth_bp
    from app.routes.ocorrencias import ocorrencias_bp
    
    # Registra os Blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(operadoras_bp)
    app.register_blueprint(cidades_bp)
    app.register_blueprint(circuitos_bp)
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(ocorrencias_bp)    
    register_error_handlers(app)
    

    return app
