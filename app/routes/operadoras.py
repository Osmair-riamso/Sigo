from flask import Blueprint, render_template, request, redirect, url_for

from app import db
from app.models import Operadora

operadoras_bp = Blueprint("operadoras", __name__)


@operadoras_bp.route("/operadoras", methods=["GET", "POST"])
def lista_operadoras():

    if request.method == "POST":

        nome = request.form["nome"].strip()

        if nome:

            operadora = Operadora(nome=nome)

            db.session.add(operadora)

            db.session.commit()

        return redirect(url_for("operadoras.lista_operadoras"))

    operadoras = Operadora.query.order_by(Operadora.nome).all()

    return render_template(
        "operadoras/lista.html",
        operadoras=operadoras
    )
