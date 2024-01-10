FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

# CMD python manage.py runserver 0.0.0.0:8000


