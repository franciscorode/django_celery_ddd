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

- Access the following pages:
  - [Admin website](http://localhost:8010/admin)
  - [API documentation](http://localhost:8010/swagger/)

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
