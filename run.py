from pathlib import Path

from app import create_app, db

app = create_app()

# Garante que a pasta instance exista
Path(app.instance_path).mkdir(parents=True, exist_ok=True)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)