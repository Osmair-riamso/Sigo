from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INSTANCE_DIR = BASE_DIR / "instance"
DATABASE_FILE = INSTANCE_DIR / "sigo.db"


class Config:
    SECRET_KEY = "trocar-esta-chave-na-producao"

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE_FILE.resolve()}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False