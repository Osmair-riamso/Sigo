from functools import wraps

from flask import (
    abort,
    redirect,
    url_for,
)

from flask_login import current_user


def admin_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if not current_user.is_authenticated:

            return redirect(
                url_for("auth.login")
            )

        if current_user.perfil != "ADMIN":

            abort(403)

        return func(*args, **kwargs)

    return wrapper
