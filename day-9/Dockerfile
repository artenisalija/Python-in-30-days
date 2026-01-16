# Docker runs pytest so you don't need it locally

FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install pytest

CMD ["pytest"]
