FROM python:3.9

WORKDIR /app
RUN apt-get update &&\
 apt-get install -y binutils libproj-dev gdal-bin &&\
 pip3 install poetry &&\
 poetry config virtualenvs.create false

COPY pyproject.toml .
RUN poetry install
