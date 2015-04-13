FROM python:2.7

# update.

RUN apt-get  install -y git
RUN mkdir /code
WORKDIR /code
RUN cd /code
RUN git clone https://github.com/WPH95/harbour-agent.git agent
CMD python agent/agent.py


