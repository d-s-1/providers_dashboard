# using a multi-stage build in an effort to keep the size of the docker image smaller


FROM python:3.7.10-alpine3.13 AS db_build

RUN apk add --no-cache --update \
    p7zip \
    sqlite

# create database from a zipped (using 7-Zip) sql file
COPY create_db_sql.7z create_db_sql.7z
# (extract)
RUN 7z e create_db_sql.7z
RUN sqlite3 app.db < utilization.sql

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

FROM python:3.7.10-alpine3.13 AS final_build

# add packages necessary to build Numpy
RUN apk add --no-cache --update \
    gcc \
    gfortran \
    musl-dev \
    libffi-dev \
    openssl-dev

RUN pip install --upgrade pip

WORKDIR /home/dashboard

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

# copy app.db from prior build
COPY --from=db_build app.db app.db

# set environment variable so that output is sent straight to terminal/container log without first being buffered
ENV PYTHONUNBUFFERED 1

ENV FLASK_APP dashboard.py
ENV FLASK_CONFIG production

COPY app app
COPY boot.sh boot.sh
COPY config.py config.py
COPY dashboard.py dashboard.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]