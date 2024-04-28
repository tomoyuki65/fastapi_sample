# 軽量版のイメージを使用
FROM python:3.12.3-slim-bullseye

WORKDIR /code

# パッケージ管理用のpoetryをインストール
RUN pip3 install poetry

# poetry.lockから依存パッケージをインストール
COPY ./pyproject.toml /code/pyproject.toml
COPY ./poetry.lock /code/poetry.lock
RUN poetry install

WORKDIR /code/src

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]