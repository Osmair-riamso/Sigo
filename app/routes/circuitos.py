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
    Circuito,
    Cidade,
    Operadora,
    Ocorrencia,
)

circuitos_bp = Blueprint("circuitos", __name__)


@circuitos_bp.route("/circuitos", methods=["GET", "POST"])
def lista_circuitos():

    editar = None

    editar_id = request.args.get("editar")

    if editar_id:
        editar = Circuito.query.get_or_404(editar_id)

    if request.method == "POST":

        circuito_id = request.form.get("id")

        cidade_id = int(request.form["cidade"])
        operadora_id = int(request.form["operadora"])
        tipo = request.form["tipo"].strip()
        designacao = request.form["designacao"].strip()

        # ======================================
        # EDITAR
        # ======================================

        if circuito_id:

            circuito = Circuito.query.get_or_404(circuito_id)

            existente = Circuito.query.filter(
                Circuito.cidade_id == cidade_id,
                Circuito.operadora_id == operadora_id,
                Circuito.designacao == designacao,
                Circuito.id != circuito.id,
            ).first()

            if existente:

                flash(
                    "Já existe um circuito com esta designação para esta operadora nesta cidade.",
                    "warning",
                )

                return redirect(
                    url_for("circuitos.lista_circuitos")
                )

            circuito.cidade_id = cidade_id
            circuito.operadora_id = operadora_id
            circuito.tipo = tipo
            circuito.designacao = designacao

            db.session.commit()

            flash(
                "Circuito atualizado com sucesso.",
                "success",
            )

            return redirect(
                url_for("circuitos.lista_circuitos")
            )

        # ======================================
        # NOVO
        # ======================================

        existente = Circuito.query.filter_by(
            cidade_id=cidade_id,
            operadora_id=operadora_id,
            designacao=designacao,
        ).first()

        if existente:

            flash(
                "Já existe um circuito com esta designação para esta operadora nesta cidade.",
                "warning",
            )

            return redirect(
                url_for("circuitos.lista_circuitos")
            )

        novo = Circuito(
            cidade_id=cidade_id,
            operadora_id=operadora_id,
            tipo=tipo,
            designacao=designacao,
            ativo=True,
        )

        db.session.add(novo)

        db.session.commit()

        flash(
            "Circuito cadastrado com sucesso.",
            "success",
        )

        return redirect(
            url_for("circuitos.lista_circuitos")
        )

    circuitos = Circuito.query.order_by(
        Circuito.id.desc()
    ).all()

    cidades = Cidade.query.filter_by(
        ativo=True
    ).order_by(
        Cidade.cidade
    ).all()

    operadoras = Operadora.query.filter_by(
        ativo=True
    ).order_by(
        Operadora.nome
    ).all()

    return render_template(
        "circuitos/lista.html",
        circuitos=circuitos,
        cidades=cidades,
        operadoras=operadoras,
        editar=editar,
    )


# ======================================
# ATIVAR / INATIVAR
# ======================================

@circuitos_bp.route(
    "/circuitos/<int:id>/status",
    methods=["POST"],
)
def alterar_status(id):

    circuito = Circuito.query.get_or_404(id)

    circuito.ativo = not circuito.ativo

    db.session.commit()

    if circuito.ativo:

        flash(
            "Circuito ativado com sucesso.",
            "success",
        )

    else:

        flash(
            "Circuito inativado com sucesso.",
            "success",
        )

    return redirect(
        url_for("circuitos.lista_circuitos")
    )


# ======================================
# EXCLUIR
# ======================================

@circuitos_bp.route(
    "/circuitos/<int:id>/excluir",
    methods=["POST"],
)
def excluir_circuito(id):

    circuito = Circuito.query.get_or_404(id)

    if circuito.ativo:

        flash(
            "Primeiro inative o circuito para poder excluí-lo.",
            "warning",
        )

        return redirect(
            url_for("circuitos.lista_circuitos")
        )

    ocorrencia = Ocorrencia.query.filter_by(
        circuito_id=id
    ).first()

    if ocorrencia:

        flash(
            "Não é possível excluir. Existem ocorrências vinculadas.",
            "danger",
        )

        return redirect(
            url_for("circuitos.lista_circuitos")
        )

    db.session.delete(circuito)

    db.session.commit()

    flash(
        "Circuito excluído definitivamente.",
        "success",
    )

    return redirect(
        url_for("circuitos.lista_circuitos")
    )
    