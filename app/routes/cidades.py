from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)

from app import db
from app.models import Cidade, Circuito

cidades_bp = Blueprint("cidades", __name__)


@cidades_bp.route("/cidades", methods=["GET", "POST"])
def lista_cidades():

    editar = None

    editar_id = request.args.get("editar")

    if editar_id:
        editar = Cidade.query.get_or_404(editar_id)

    if request.method == "POST":

        cidade = request.form["cidade"].strip().upper()
        estado = request.form["estado"].strip().upper()

        cidade_id = request.form.get("id")

        # ==========================
        # EDITAR
        # ==========================

        if cidade_id:

            registro = Cidade.query.get_or_404(cidade_id)

            existente = Cidade.query.filter(
                Cidade.cidade == cidade,
                Cidade.estado == estado,
                Cidade.id != registro.id,
            ).first()

            if existente:

                flash(
                    "Esta cidade já está cadastrada.",
                    "warning",
                )

                return redirect(
                    url_for("cidades.lista_cidades")
                )

            registro.cidade = cidade
            registro.estado = estado

            db.session.commit()

            flash(
                "Cidade atualizada com sucesso.",
                "success",
            )

            return redirect(
                url_for("cidades.lista_cidades")
            )

        # ==========================
        # NOVO
        # ==========================

        existente = Cidade.query.filter_by(
            cidade=cidade,
            estado=estado,
        ).first()

        if existente:

            flash(
                "Cidade já cadastrada.",
                "warning",
            )

            return redirect(
                url_for("cidades.lista_cidades")
            )

        nova = Cidade(
            cidade=cidade,
            estado=estado,
        )

        db.session.add(nova)
        db.session.commit()

        flash(
            "Cidade cadastrada com sucesso.",
            "success",
        )

        return redirect(
            url_for("cidades.lista_cidades")
        )

    cidades = Cidade.query.order_by(
        Cidade.estado,
        Cidade.cidade,
    ).all()

    return render_template(
        "cidades/lista.html",
        cidades=cidades,
        editar=editar,
    )


@cidades_bp.route(
    "/cidades/<int:id>/excluir",
    methods=["POST"],
)
def excluir_cidade(id):

    cidade = Cidade.query.get_or_404(id)

    circuito = Circuito.query.filter_by(
        cidade_id=id
    ).first()

    if circuito:

        flash(
            "Não é possível excluir esta cidade porque existem circuitos vinculados.",
            "danger",
        )

        return redirect(
            url_for("cidades.lista_cidades")
        )

    db.session.delete(cidade)

    db.session.commit()

    flash(
        "Cidade excluída com sucesso.",
        "success",
    )

    return redirect(
        url_for("cidades.lista_cidades")
    )
    
    