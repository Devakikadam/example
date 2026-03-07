FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache \
    postgresql-client \
    libpq-dev \
    gcc \
    musl-dev

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /snet

COPY pyproject.toml uv.lock* /snet/

RUN uv pip install --system --no-cache -r pyproject.toml

COPY . /snet/

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]