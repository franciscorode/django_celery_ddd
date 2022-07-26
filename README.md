# 🤖 Umibot

UmiShop bots management

## 💻 Set up

1. 🐱 Get the repository

```shell
git clone git@github.com:franciscorode/umibot.git
```

2. 🏗️ Create a virtual environment

```shell
python3.9 -m virtualenv venv
. venv/bin/activate
```

3. 📥 Install the dependencies

```shell
make install
```

4. 🔛 Enable pre-commit hooks

```shell
pre-commit install
```

## 🚀 Build application

```shell
make up
```

### 🌐 Access the following pages

- [Admin website](http://localhost:8010/admin)
- [API documentation](http://localhost:8010/swagger/)
- [Celery flower](http://localhost:5557/)

### 🌎 Environment variables

It needs to declare the next environment variables in a `.env` file

- Required

  - `ENVIRONMENT_NAME=LOCAL`
  - `POSTGRES_USER=appuser`
  - `POSTGRES_PASSWORD=password`
  - `EMAIL_HOST_USER=example@example.com`
  - `EMAIL_HOST_PASSWORD=password`
  - `CUSTOMER_SUPPORT_EMAIL=support@example.com`
  - `SLACK_CHANNEL=channel|channel_id`
  - `SLACK_TOKEN=token`

- Optional

  - `DJANGO_DEBUG=true`
  - `DJANGO_DEBUG_PORT=8010`
  - `POSTGRES_PORT=5555`

## ✔️ Test

```shell
make up
make test
```

## 🧹 Lint

```shell
make lint
```

## 🌟 Format

```shell
make format
```
