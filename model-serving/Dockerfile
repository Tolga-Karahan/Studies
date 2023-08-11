FROM python:3.9.13-slim-buster

RUN mkdir /adjoe-task

COPY adjoe_task /adjoe-task/adjoe_task

COPY requirements.txt /adjoe-task

WORKDIR /adjoe-task

RUN pip install pip --upgrade && pip install -r requirements.txt

RUN chmod +x adjoe_task/start.sh

EXPOSE 8000

CMD ["/bin/bash", "adjoe_task/start.sh"]