FROM python:3.9-alpine3.18

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /temp/requirements.txt
COPY . /app

WORKDIR /app

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password service-user

USER service-user

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
