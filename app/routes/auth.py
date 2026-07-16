from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)

from flask_login import (
    login_user,
    logout_user,
    current_user,
)

from app.models import Usuario

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))

    if request.method == "POST":

        login = request.form["login"].strip().lower()
        senha = request.form["senha"]

        usuario = Usuario.query.filter_by(
            login=login,
            ativo=True,
        ).first()

        if not usuario or not usuario.verificar_senha(senha):

            flash(
                "Usuário ou senha inválidos.",
                "danger",
            )

            return redirect(
                url_for("auth.login")
            )

        login_user(usuario)

        flash(
            f"Bem-vindo, {usuario.nome}.",
            "success",
        )

        return redirect(
            url_for("main.dashboard")
        )

    return render_template("auth/login.html")


@auth_bp.route("/logout")
def logout():

    logout_user()

    flash(
        "Logout realizado com sucesso.",
        "success",
    )

    return redirect(
        url_for("main.dashboard")
    )
    