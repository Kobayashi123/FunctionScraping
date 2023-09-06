FROM python:3.11.5 as builder
WORKDIR /app
RUN apt-get update && apt-get upgrade -y && apt-get install -y vim && apt-get autoremove -y
RUN pip install --no-cache-dir --upgrade pip
COPY ./develop.txt /tmp/
RUN pip install -r /tmp/develop.txt
COPY ./pyproject.toml /app/
COPY ./setup.cfg /app/
COPY ./Makefile /app/
COPY ./requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
COPY ./src /app/src
CMD [ "/bin/bash" ]

FROM python:3.11.4-slim-bullseye
WORKDIR /app/src
RUN apt-get update && apt-get upgrade -y && apt-get install -y vim && apt-get autoremove -y
RUN pip install --no-cache-dir --upgrade pip
COPY ./requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
COPY ./src /app/src
CMD [ "python", "example.py" ]
