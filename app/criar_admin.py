from app import create_app, db
from app.models import Usuario

app = create_app()

with app.app_context():

    # verifica se já existe
    admin_existente = Usuario.query.filter_by(login="admin").first()

    if admin_existente:
        print("Usuário admin já existe!")
    else:
        admin = Usuario(
            nome="Administrador",
            login="admin",
            perfil="ADMIN"
        )

        admin.definir_senha("123456")

        db.session.add(admin)
        db.session.commit()

        print("================================")
        print("Administrador criado com sucesso!")
        print("Login: admin")
        print("Senha: 123456")
        print("Perfil: ADMIN")
        print("================================")
        