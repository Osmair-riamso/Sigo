from datetime import datetime

from . import db


def agora():
    """Retorna a data e hora atual."""
    return datetime.utcnow()


class BaseModel(db.Model):
    """
    Classe base para todas as tabelas do sistema.
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
    