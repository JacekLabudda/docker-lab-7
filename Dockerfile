FROM python:3.12-slim AS base

WORKDIR /app

COPY app.py .


FROM base AS test

COPY test_app.py .

RUN pip install pytest

CMD ["pytest"]


FROM base AS prod

CMD ["python", "app.py"]
