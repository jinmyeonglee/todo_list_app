FROM ubuntu:18.04

USER root

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get install -y python3 python3-pip

COPY . /
EXPOSE 8080

RUN python3 -m pip install -r requirements.txt

RUN echo "$OPEN_RC" > openrc
RUN echo "$OPEN_RC_PWD" > pwd
RUN chmod +x openrc
RUN ./openrc < pwd

CMD ["python3 app.py"]