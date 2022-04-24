FROM python:3.8.3-alpine

RUN mkdir /app
WORKDIR /app

COPY . .

ENV PYTHONPATH /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -Ur requirements.txt

ENTRYPOINT ["python", "main.py"]