FROM python:3

WORKDIR /src

COPY /config/db/src/Encuesta ../db/Encuesta

COPY /src/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
