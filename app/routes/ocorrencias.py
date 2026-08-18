from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)

from flask_login import login_required, current_user

from app import db
from app.models import (
    Ocorrencia,
    Cidade,
    Circuito,
    Operadora,
    HistoricoOcorrencia,
)


ocorrencias_bp = Blueprint(
    "ocorrencias",
    __name__,
)


# ==========================================================
# LISTAGEM
# ==========================================================

@ocorrencias_bp.route("/ocorrencias")
@login_required
def lista_ocorrencias():

    ocorrencias = Ocorrencia.query.order_by(
        Ocorrencia.created_at.desc()
    ).all()

    return render_template(
        "ocorrencias/lista.html",
        ocorrencias=ocorrencias,
    )


# ==========================================================
# NOVA OCORRÊNCIA
# ==========================================================

@ocorrencias_bp.route(
    "/ocorrencias/nova",
    methods=["GET", "POST"],
)
@login_required
def nova_ocorrencia():

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

    circuitos = Circuito.query.filter_by(
        ativo=True
    ).order_by(
        Circuito.designacao
    ).all()

    if request.method == "POST":

        cidade_id = request.form.get("cidade_id")
        circuito_id = request.form.get("circuito_id")
        operadora_id = request.form.get("operadora_id")

        protocolo = request.form.get(
            "protocolo",
            ""
        ).strip()

        tipo = request.form.get(
            "tipo",
            ""
        ).strip()

        prioridade = request.form.get(
            "prioridade",
            ""
        ).strip()

        sintoma = request.form.get(
            "sintoma",
            ""
        ).strip()

        tecnico = request.form.get(
            "tecnico",
            ""
        ).strip()

        previsao = request.form.get(
            "previsao",
            ""
        ).strip()

        observacao = request.form.get(
            "observacao",
            ""
        ).strip()

        if not cidade_id or not circuito_id or not operadora_id:
            flash(
                "Cidade, circuito e operadora são obrigatórios.",
                "warning",
            )

            return render_template(
                "ocorrencias/formulario.html",
                cidades=cidades,
                operadoras=operadoras,
                circuitos=circuitos,
            )

        if not tipo or not prioridade or not sintoma:
            flash(
                "Tipo, prioridade e sintoma são obrigatórios.",
                "warning",
            )

            return render_template(
                "ocorrencias/formulario.html",
                cidades=cidades,
                operadoras=operadoras,
                circuitos=circuitos,
            )

        ocorrencia = Ocorrencia(
            cidade_id=int(cidade_id),
            circuito_id=int(circuito_id),
            operadora_id=int(operadora_id),
            usuario_id=current_user.id,
            protocolo=protocolo or None,
            tipo=tipo,
            prioridade=prioridade,
            sintoma=sintoma,
            status="ABERTA",
            tecnico=tecnico or None,
            previsao=previsao or None,
            observacao=observacao or None,
            tecnico_campo=False,
        )

        db.session.add(ocorrencia)
        db.session.flush()

        historico = HistoricoOcorrencia(
            ocorrencia_id=ocorrencia.id,
            usuario_id=current_user.id,
            descricao="Ocorrência criada.",
        )

        db.session.add(historico)

        db.session.commit()

        flash(
            "Ocorrência cadastrada com sucesso.",
            "success",
        )

        return redirect(
            url_for(
                "ocorrencias.detalhes_ocorrencia",
                id=ocorrencia.id,
            )
        )

    return render_template(
        "ocorrencias/formulario.html",
        cidades=cidades,
        operadoras=operadoras,
        circuitos=circuitos,
    )


# ==========================================================
# DETALHES
# ==========================================================

@ocorrencias_bp.route(
    "/ocorrencias/<int:id>"
)
@login_required
def detalhes_ocorrencia(id):

    ocorrencia = Ocorrencia.query.get_or_404(id)

    historico = HistoricoOcorrencia.query.filter_by(
        ocorrencia_id=id
    ).order_by(
        HistoricoOcorrencia.created_at.desc()
    ).all()

    return render_template(
        "ocorrencias/detalhes.html",
        ocorrencia=ocorrencia,
        historico=historico,
    )
# ==========================================================
# ATUALIZAR OCORRÊNCIA
# ==========================================================

@ocorrencias_bp.route(
    "/ocorrencias/<int:id>/atualizar",
    methods=["POST"],
)
@login_required
def atualizar_ocorrencia(id):

    ocorrencia = Ocorrencia.query.get_or_404(id)

    status = request.form.get(
        "status",
        ""
    ).strip()

    tecnico = request.form.get(
        "tecnico",
        ""
    ).strip()

    previsao = request.form.get(
        "previsao",
        ""
    ).strip()

    tecnico_campo = request.form.get(
        "tecnico_campo"
    )

    observacao = request.form.get(
        "observacao",
        ""
    ).strip()

    if not status:
        flash(
            "O status da ocorrência é obrigatório.",
            "warning",
        )

        return redirect(
            url_for(
                "ocorrencias.detalhes_ocorrencia",
                id=id,
            )
        )

    ocorrencia.status = status

    ocorrencia.tecnico = (
        tecnico or None
    )

    ocorrencia.previsao = (
        previsao or None
    )

    ocorrencia.tecnico_campo = (
        tecnico_campo == "sim"
    )

    if observacao:

        ocorrencia.observacao = observacao

        historico = HistoricoOcorrencia(
            ocorrencia_id=ocorrencia.id,
            usuario_id=current_user.id,
            descricao=observacao,
        )

        db.session.add(historico)

    db.session.commit()

    flash(
        "Ocorrência atualizada com sucesso.",
        "success",
    )

    return redirect(
        url_for(
            "ocorrencias.detalhes_ocorrencia",
            id=id,
        )
    )