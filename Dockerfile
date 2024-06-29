FROM python:3.11-bookworm

WORKDIR /app

# install PDM
RUN pip install -U pdm
# disable update check
ENV PDM_CHECK_UPDATE=false

COPY pdm.lock pyproject.toml ./
RUN pdm install

COPY ./src ./src
COPY ./tests ./tests
COPY .devcontainer .devcontainer

RUN apt-get update
RUN apt-get install -y sqlite3 libsqlite3-dev
RUN pdm run -v src/db_setup.py

EXPOSE 8080

CMD ["pdm", "run", "uvicorn", "src.de_pdm.__init__:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
