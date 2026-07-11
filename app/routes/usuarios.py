from flask import Blueprint, render_template, request, redirect, url_for

from app import db
from app.models import Usuario

usuarios_bp = Blueprint("usuarios", __name__)


@usuarios_bp.route("/usuarios", methods=["GET", "POST"])
def lista_usuarios():

    if request.method == "POST":

        usuario = Usuario(

            nome=request.form["nome"],

            login=request.form["login"],

            perfil=request.form["perfil"]

        )

        usuario.definir_senha(request.form["senha"])

        db.session.add(usuario)

        db.session.commit()

        return redirect(url_for("usuarios.lista_usuarios"))

    usuarios = Usuario.query.order_by(Usuario.nome).all()

    return render_template(
        "usuarios/lista.html",
        usuarios=usuarios
    )
    