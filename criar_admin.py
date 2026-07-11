from app import create_app, db
from app.models import Usuario

app = create_app()


def criar_admin():
    with app.app_context():

        usuario = Usuario.query.filter_by(login="admin").first()

        if usuario:
            print("Administrador já existe.")
            return

        admin = Usuario(
            nome="Administrador",
            login="admin",
            perfil="ADMIN",
        )

        admin.definir_senha("admin123")

        db.session.add(admin)
        db.session.commit()

        print("Administrador criado com sucesso!")
        print("Login: admin")
        print("Senha: admin123")


if __name__ == "__main__":
    criar_admin()
    