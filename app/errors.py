from flask import render_template


def register_error_handlers(app):

    @app.errorhandler(401)
    def erro401(e):
        return render_template(
            "errors/401.html"
        ), 401

    @app.errorhandler(403)
    def erro403(e):
        return render_template(
            "errors/403.html"
        ), 403

    @app.errorhandler(404)
    def erro404(e):
        return render_template(
            "errors/404.html"
        ), 404

    @app.errorhandler(500)
    def erro500(e):
        return render_template(
            "errors/500.html"
        ), 500
        