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
    
class Cidade(BaseModel):
    """
    Cadastro de cidades atendidas.
    """

    __tablename__ = "cidades"

    cidade = db.Column(
        db.String(100),
        nullable=False,
    )

    estado = db.Column(
        db.String(2),
        nullable=False,
    )

    def __repr__(self):
        return f"<Cidade {self.cidade}/{self.estado}>"



class Circuito(BaseModel):
    """
    Cadastro dos circuitos de fibra.
    """

    __tablename__ = "circuitos"

    cidade_id = db.Column(
        db.Integer,
        db.ForeignKey("cidades.id"),
        nullable=False,
    )

    operadora_id = db.Column(
        db.Integer,
        db.ForeignKey("operadoras.id"),
        nullable=False,
    )

    tipo = db.Column(
        db.String(20),
        nullable=False,
    )  # Principal | Redundante

    designacao = db.Column(
        db.String(150),
        nullable=False,
    )

    observacao = db.Column(
        db.String(255),
        nullable=True,
    )

    cidade = db.relationship("Cidade")

    operadora = db.relationship("Operadora")

    def __repr__(self):
        return (
            f"<Circuito "
            f"{self.cidade.cidade}/{self.cidade.estado} - "
            f"{self.tipo} - "
            f"{self.operadora.nome}>"
        )



class Ocorrencia(BaseModel):
    """
    Chamado principal do sistema.
    """

    __tablename__ = "ocorrencias"

    circuito_id = db.Column(
        db.Integer,
        db.ForeignKey("circuitos.id"),
        nullable=False,
    )

    usuario_abertura_id = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id"),
        nullable=False,
    )

    protocolo = db.Column(
        db.String(80)
    )

    prioridade = db.Column(
        db.String(30),
        nullable=False,
    )

    status = db.Column(
        db.String(30),
        nullable=False,
        default="Aberto"
    )

    sintoma = db.Column(
        db.String(200),
        nullable=False,
    )

    tecnico_campo = db.Column(
        db.Boolean,
        default=False,
    )

    data_abertura = db.Column(
        db.DateTime,
        default=agora,
        nullable=False,
    )

    data_encerramento = db.Column(
        db.DateTime
    )

    circuito = db.relationship("Circuito")

    usuario_abertura = db.relationship("Usuario")

    def __repr__(self):
        return f"<Ocorrencia {self.id}>"