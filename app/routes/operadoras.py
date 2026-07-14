from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)

from app import db
from app.models import Operadora, Circuito

operadoras_bp = Blueprint("operadoras", __name__)


@operadoras_bp.route("/operadoras", methods=["GET", "POST"])
def lista_operadoras():

    editar = None

    editar_id = request.args.get("editar")

    if editar_id:
        editar = Operadora.query.get_or_404(editar_id)

    if request.method == "POST":

        operadora_id = request.form.get("id")
        nome = request.form["nome"].strip()

        # ==========================
        # EDITAR
        # ==========================

        if operadora_id:

            operadora = Operadora.query.get_or_404(operadora_id)

            existente = Operadora.query.filter(
                Operadora.nome == nome,
                Operadora.id != operadora.id,
            ).first()

            if existente:

                flash(
                    "Já existe uma operadora com este nome.",
                    "warning",
                )

                return redirect(
                    url_for("operadoras.lista_operadoras")
                )

            operadora.nome = nome

            db.session.commit()

            flash(
                "Operadora atualizada com sucesso.",
                "success",
            )

            return redirect(
                url_for("operadoras.lista_operadoras")
            )

        # ==========================
        # NOVA
        # ==========================

        existente = Operadora.query.filter_by(
            nome=nome
        ).first()

        if existente:

            flash(
                "Operadora já cadastrada.",
                "warning",
            )

            return redirect(
                url_for("operadoras.lista_operadoras")
            )

        nova = Operadora(
            nome=nome,
            ativo=True,
        )

        db.session.add(nova)

        db.session.commit()

        flash(
            "Operadora cadastrada com sucesso.",
            "success",
        )

        return redirect(
            url_for("operadoras.lista_operadoras")
        )

    operadoras = Operadora.query.order_by(
        Operadora.nome
    ).all()

    return render_template(
        "operadoras/lista.html",
        operadoras=operadoras,
        editar=editar,
    )


# ==========================
# ATIVAR / INATIVAR
# ==========================

@operadoras_bp.route(
    "/operadoras/<int:id>/status",
    methods=["POST"],
)
def alterar_status(id):

    operadora = Operadora.query.get_or_404(id)

    operadora.ativo = not operadora.ativo

    db.session.commit()

    if operadora.ativo:

        flash(
            "Operadora ativada com sucesso.",
            "success",
        )

    else:

        flash(
            "Operadora inativada com sucesso.",
            "success",
        )

    return redirect(
        url_for("operadoras.lista_operadoras")
    )


# ==========================
# EXCLUIR
# ==========================

@operadoras_bp.route(
    "/operadoras/<int:id>/excluir",
    methods=["POST"],
)
def excluir_operadora(id):

    operadora = Operadora.query.get_or_404(id)

    if operadora.ativo:

        flash(
            "Primeiro inative a operadora para poder excluí-la.",
            "warning",
        )

        return redirect(
            url_for("operadoras.lista_operadoras")
        )

    circuito = Circuito.query.filter_by(
        operadora_id=id
    ).first()

    if circuito:

        flash(
            "Não é possível excluir. Existem circuitos vinculados.",
            "danger",
        )

        return redirect(
            url_for("operadoras.lista_operadoras")
        )

    db.session.delete(operadora)

    db.session.commit()

    flash(
        "Operadora excluída definitivamente.",
        "success",
    )

    return redirect(
        url_for("operadoras.lista_operadoras")
    )
    