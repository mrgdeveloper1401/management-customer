from decouple import config


class Config:
    SECRET_KEY = config("SECRET_KEY", default="default-secret", cast=str)

    POSTGRES_NAME = config("POSTDB_NAME", cast=str, default="complaintsdb")
    POSTGRES_PASSWORD = config("POSTDB_PASSWORD", cast=str, default="postgres")
    POSTGRES_HOST = config("POSTDB_HOST", cast=str, default="localhost")
    POSTGRES_PORT = config("POSTDB_PORT", cast=int, default=5432)
    POSTGRES_USER = config("POSTDB_USER", cast=str, default="postgres")

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{POSTGRES_USER}:"
        f"{POSTGRES_PASSWORD}@"
        f"{POSTGRES_HOST}:"
        f"{POSTGRES_PORT}/"
        f"{POSTGRES_NAME}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
