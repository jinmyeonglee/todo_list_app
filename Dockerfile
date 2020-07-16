#FROM python:3.7
#MAINTAINER Jinmyeong "jinmyeong.lee@linecorp.com"
#RUN mkdir /app
#WORKDIR /app
#ADD . /app/
#RUN pip install -r requirements.txt
#EXPOSE 5000
#CMD ["./app/start.sh"]

FROM ubuntu:18.04

# 사용자 지정
USER root

# 기본적으로 필요한 OS 패키지를 설치한다.
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get install -y python3 python3-pip

ADD . /
#WORKDIR /app
RUN chmod +x start.sh
RUN chmod +x openrc-2b547e4137ab40ac871ffbdbc5d9f3e9-jp2
RUN ./openrc-2b547e4137ab40ac871ffbdbc5d9f3e9-jp2 < password
RUN python3 -m pip install -r requirements.txt

# 컨테이너 실행시 실행될 명령
CMD ["./start.sh"]
#CMD ["/bin/bash"]