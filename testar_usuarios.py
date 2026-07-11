from app import create_app
from app.models import Usuario

app = create_app()

with app.app_context():
    usuarios = Usuario.query.all()

    print("\nUsuários cadastrados:\n")

    for usuario in usuarios:
        print(
            f"ID: {usuario.id} | "
            f"Nome: {usuario.nome} | "
            f"Login: {usuario.login} | "
            f"Perfil: {usuario.perfil}"
        )
        