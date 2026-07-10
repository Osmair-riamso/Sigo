from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class Config:
    SECRET_KEY = "trocar-esta-chave-na-producao"

    SQLALCHEMY_DATABASE_URI = (
        f"sqlite:///{BASE_DIR / 'instance' / 'sigo.db'}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    