from flask import Blueprint, render_template, request, redirect, url_for

from app import db
from app.models import Circuito, Cidade, Operadora

circuitos_bp = Blueprint("circuitos", __name__)


@circuitos_bp.route("/circuitos", methods=["GET", "POST"])
def lista_circuitos():

    if request.method == "POST":

        circuito = Circuito(

            cidade_id=request.form["cidade"],

            operadora_id=request.form["operadora"],

            tipo=request.form["tipo"],

            designacao=request.form["designacao"],

            ativo=True

        )

        db.session.add(circuito)

        db.session.commit()

        return redirect(url_for("circuitos.lista_circuitos"))

    circuitos = Circuito.query.order_by(Circuito.id.desc()).all()

    cidades = Cidade.query.order_by(Cidade.cidade).all()

    operadoras = Operadora.query.order_by(Operadora.nome).all()

    return render_template(

        "circuitos/lista.html",

        circuitos=circuitos,

        cidades=cidades,

        operadoras=operadoras

    )
    