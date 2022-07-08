FROM python:3.9.13-slim-buster

RUN mkdir /app 

COPY src app/src

COPY requirements.txt /app

WORKDIR /app

RUN pip install pip --upgrade && pip install -r requirements.txt

RUN chmod +x src/start.sh

EXPOSE 8000

CMD ["/bin/bash", "src/start.sh"]