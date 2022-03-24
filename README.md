# Apptrix test task

Тестовое задание apptrix

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
