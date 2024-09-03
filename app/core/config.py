import os
import psycopg2

from starlette.config import Config

ROOT_DIR = os.getcwd()
_config = Config(os.path.join(ROOT_DIR, ".env"))
APP_VERSION = "0.0.1"
APP_NAME = "APP_name"
API_PREFIX = ""

# Env vars
IS_DEBUG: bool = _config("IS_DEBUG", cast=bool, default=False)

DB_URL: str = _config("DB_URL", cast=str, default="sqlite:///./sql_app.db")
CHANNELS: str = "sms,email,push"


def get_celery_broker_url():
    """Generate the broker url from the environment."""
    protocol = _config("CELERY_BROKER_PROTOCOL", cast=str, default="")
    username = _config("CELERY_BROKER_USERNAME", default="")
    password = _config("CELERY_BROKER_PASSWORD", cast=str, default="")
    host = _config("CELERY_BROKER_HOST", cast=str, default="")
    port = _config("CELERY_BROKER_PORT", cast=str, default="")
    db = _config("CELERY_BROKER_DB", cast=str, default="")
    return f"{protocol}://{username}:{password}@{host}:{port}/{db}"


# Celery
CELERY_BROKER_URL: str = get_celery_broker_url()


def get_connection():

    host = _config("DB_HOST", cast=str, default="")
    port = _config("DB_PORT", cast=str, default="")
    database = _config("DB_NAME", cast=str, default="")
    user = _config("DB_USERNAME", cast=str, default="")
    password = _config("DB_PASSWORD", cast=str, default="")

    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )

    return conn
