import decouple

__all__ = [
    "ADVICE_CHAT_ID",
    "GROUP_TOKEN",
    "POSTGRES_URL",
    "REDIS_URL",
    "TORTOISE_ORM",
]

GROUP_TOKEN = decouple.config("GROUP_TOKEN", cast=str)
ADVICE_CHAT_ID = decouple.config("ADVICE_CHAT_ID", cast=int)

REDIS_HOST = decouple.config("REDIS_HOST", cast=str)
REDIS_PORT = decouple.config("REDIS_PORT", cast=int)

REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}"

POSTGRES_HOST = decouple.config("POSTGRES_HOST", cast=str)
POSTGRES_PORT = decouple.config("POSTGRES_PORT", cast=int)
POSTGRES_PASSWORD = decouple.config("POSTGRES_PASSWORD", cast=str)
POSTGRES_USER = decouple.config("POSTGRES_USER", cast=str)
POSTGRES_DB = decouple.config("POSTGRES_DB", cast=str)

POSTGRES_URL = f"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

TORTOISE_ORM = {
    "connections": {"default": POSTGRES_URL},
    "apps": {
        "models": {
            "models": ["source.database.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
