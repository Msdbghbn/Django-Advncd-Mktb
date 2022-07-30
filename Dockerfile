FROM python:3.8-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update -y
RUN apt-get install python3-tk -y
COPY ./core /app