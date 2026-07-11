from flask import Blueprint, render_template, request, redirect, url_for

from app import db
from app.models import Cidade

cidades_bp = Blueprint("cidades", __name__)


@cidades_bp.route("/cidades", methods=["GET", "POST"])
def lista_cidades():

    if request.method == "POST":

        cidade = request.form["cidade"].strip()
        estado = request.form["estado"].strip().upper()

        if cidade and estado:

            nova = Cidade(
                cidade=cidade,
                estado=estado
            )

            db.session.add(nova)
            db.session.commit()

        return redirect(url_for("cidades.lista_cidades"))

    cidades = Cidade.query.order_by(Cidade.cidade).all()

    return render_template(
        "cidades/lista.html",
        cidades=cidades
    )
    