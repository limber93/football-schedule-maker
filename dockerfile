FROM python:3.9

ENV PYTHONUNBUFFERED=1

RUN apt update && apt install -y \
    postgresql-client libsasl2-dev python3-dev libldap2-dev libssl-dev
WORKDIR /app
ADD ./requirements.txt .
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
