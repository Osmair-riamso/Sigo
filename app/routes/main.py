from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def dashboard():

    return render_template(
        "dashboard.html",
        ocorrencias=[],
        passagem_turno=None,
        agenda=None,
        resumo=None,
        ultima_atualizacao=None,
        agenda_prioritaria=None,
        alertas=None,
    )
    
