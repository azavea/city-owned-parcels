FROM nginx:1.10-alpine

MAINTAINER Azavea

RUN mkdir -p /srv/dist && \
    chown nginx:nginx -R /srv/dist/

COPY srv/dist /srv/dist/
COPY etc/nginx/nginx.conf /etc/nginx/nginx.conf
