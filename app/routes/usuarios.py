from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)

from app import db

from app.models import (
    Usuario,
    Ocorrencia,
)
from app.decorators import admin_required

usuarios_bp = Blueprint("usuarios", __name__)


@usuarios_bp.route("/usuarios", methods=["GET", "POST"])
@admin_required
def lista_usuarios():

    editar = None

    editar_id = request.args.get("editar")

    if editar_id:
        editar = Usuario.query.get_or_404(editar_id)

    if request.method == "POST":

        usuario_id = request.form.get("id")

        nome = request.form["nome"].strip()
        login = request.form["login"].strip().lower()
        perfil = request.form["perfil"]
        senha = request.form["senha"]

        # ======================================
        # EDITAR
        # ======================================

        if usuario_id:

            usuario = Usuario.query.get_or_404(usuario_id)

            existente = Usuario.query.filter(
                Usuario.login == login,
                Usuario.id != usuario.id,
            ).first()

            if existente:

                flash(
                    "Já existe um usuário com este login.",
                    "warning",
                )

                return redirect(
                    url_for("usuarios.lista_usuarios")
                )

            usuario.nome = nome
            usuario.login = login
            usuario.perfil = perfil

            if senha:

                usuario.definir_senha(senha)

            db.session.commit()

            flash(
                "Usuário atualizado com sucesso.",
                "success",
            )

            return redirect(
                url_for("usuarios.lista_usuarios")
            )

        # ======================================
        # NOVO
        # ======================================

        existente = Usuario.query.filter_by(
            login=login
        ).first()

        if existente:

            flash(
                "Já existe um usuário com este login.",
                "warning",
            )

            return redirect(
                url_for("usuarios.lista_usuarios")
            )

        usuario = Usuario(
            nome=nome,
            login=login,
            perfil=perfil,
            ativo=True,
        )

        usuario.definir_senha(senha)

        db.session.add(usuario)

        db.session.commit()

        flash(
            "Usuário cadastrado com sucesso.",
            "success",
        )

        return redirect(
            url_for("usuarios.lista_usuarios")
        )

    usuarios = Usuario.query.order_by(
        Usuario.nome
    ).all()

    return render_template(
        "usuarios/lista.html",
        usuarios=usuarios,
        editar=editar,
    )


# ======================================
# ATIVAR / INATIVAR
# ======================================

@usuarios_bp.route(
    "/usuarios/<int:id>/status",
    methods=["POST"],
)
@admin_required
def alterar_status(id):

    usuario = Usuario.query.get_or_404(id)

    usuario.ativo = not usuario.ativo

    db.session.commit()

    if usuario.ativo:

        flash(
            "Usuário ativado com sucesso.",
            "success",
        )

    else:

        flash(
            "Usuário inativado com sucesso.",
            "success",
        )

    return redirect(
        url_for("usuarios.lista_usuarios")
    )


# ======================================
# EXCLUIR
# ======================================

@usuarios_bp.route(
    "/usuarios/<int:id>/excluir",
    methods=["POST"],
)
@admin_required
def excluir_usuario(id):

    usuario = Usuario.query.get_or_404(id)

    if usuario.ativo:

        flash(
            "Primeiro inative o usuário para poder excluí-lo.",
            "warning",
        )

        return redirect(
            url_for("usuarios.lista_usuarios")
        )

    ocorrencia = Ocorrencia.query.filter_by(
        usuario_abertura_id=id
    ).first()

    if ocorrencia:

        flash(
            "Não é possível excluir. Existem ocorrências vinculadas a este usuário.",
            "danger",
        )

        return redirect(
            url_for("usuarios.lista_usuarios")
        )

    db.session.delete(usuario)

    db.session.commit()

    flash(
        "Usuário excluído definitivamente.",
        "success",
    )

    return redirect(
        url_for("usuarios.lista_usuarios")
    )
    