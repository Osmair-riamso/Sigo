from flask import (
    Blueprint,
    render_template,
)

from flask_login import (
    login_required,
)

from app.models import Ocorrencia

ocorrencias_bp = Blueprint(
    "ocorrencias",
    __name__,
)


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
    