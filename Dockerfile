FROM python:2.7

# update.

RUN apt-get  install -y git

RUN mkdir /code
WORKDIR /code
