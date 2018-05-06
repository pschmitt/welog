FROM python:3-alpine

LABEL MAINTAINER="Philipp Schmitt <philipp@schmitt.co>"

WORKDIR /app

EXPOSE 5000

ENV FLASK_DEBUG=

ADD . /app

RUN pip install -r /app/requirements.txt

CMD ["/app/welog.py"]
