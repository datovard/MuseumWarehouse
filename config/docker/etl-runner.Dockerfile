FROM python:3

WORKDIR /src

COPY /src/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY /src/ .
COPY /config/db/src/Encuesta ./Encuesta

RUN ls

CMD [ "python", "./index.py" ]