FROM quay.io/azavea/flask:0.11

MAINTAINER Azavea

RUN apt-get update && \
    apt-get install -y \
    curl=7.38.0-4+deb8u4 \
    libpq-dev=9.4.9-0+deb8u1

RUN pip install --upgrade pip
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./api /usr/src/api
COPY ./etl /usr/src/etl

WORKDIR /usr/src/api

EXPOSE 8080

CMD ["-w", "2", \
     "-b", "0.0.0.0:8080", \
     "--reload", \
     "--log-level", "info", \
     "--error-logfile", "-", \
     "--forwarded-allow-ips", "*", \
     "-k", "gevent", \
     "main:app"]
