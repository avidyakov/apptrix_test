# Apptrix test task

Тестовое задание apptrix https://docs.google.com/document/d/1LpUf2cZdtDAZKgDP9zw7i8Qn98r7og0p8QqizZkMfhE/edit

## Installation

Чтобы запустить проект, выполните следующие команды

```bash
cat .env.temp > .env
docker compose up --build
```

После успешного запуска сервера, выполните в другом окне

```bash
docker compose exec web python manage.py migrate
```

## Usage

Последующие запуски проекта

```bash
docker compose up
```

## Docs

http://107.174.244.50:8000/docs/
