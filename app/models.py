from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from . import db


def agora():
    """Retorna a data e hora atual."""
    return datetime.utcnow()


class BaseModel(db.Model):
    """
    Classe base para todas as tabelas.
    """

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

    ativo = db.Column(
        db.Boolean,
        default=True,
        nullable=False,
    )

    created_at = db.Column(
        db.DateTime,
        default=agora,
        nullable=False,
    )

    updated_at = db.Column(
        db.DateTime,
        default=agora,
        onupdate=agora,
        nullable=False,
    )


class Operadora(BaseModel):
    """
    Cadastro de operadoras.
    """

    __tablename__ = "operadoras"

    nome = db.Column(
        db.String(100),
        unique=True,
        nullable=False,
    )

    def __repr__(self):
        return f"<Operadora {self.nome}>"


class Usuario(UserMixin, BaseModel):
    """
    Cadastro de usuários do sistema.
    """

    __tablename__ = "usuarios"

    nome = db.Column(
        db.String(120),
        nullable=False,
    )

    login = db.Column(
        db.String(50),
        unique=True,
        nullable=False,
    )

    senha_hash = db.Column(
        db.String(255),
        nullable=False,
    )

    perfil = db.Column(
        db.String(20),
        nullable=False,
        default="USER",
    )

    def definir_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def verificar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)

    def __repr__(self):
        return f"<Usuario {self.login}>"
    