FROM python:3.10-slim as base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \

    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \

    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \

    PYSETUP_PATH="/opt/pysetup" \

    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

FROM base as builder

WORKDIR $PYSETUP_PATH

RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev

FROM base as production

COPY --from=builder $VENV_PATH $VENV_PATH

WORKDIR /app
COPY . .

COPY docker-entrypoint.sh ./
ENTRYPOINT ["./docker-entrypoint.sh"]

CMD ["python", "-m", "source"]
