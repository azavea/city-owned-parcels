#!/bin/bash

set -e

if [[ -n "${COP_DEBUG}" ]]; then
    set -x
fi

usage() {
    echo -n "$(basename "${0}") [OPTION]

Login to a running Docker container\'s shell.

Options:
    flask     Flask container
    nginx     Nginx container
    database  psql shell in database container
    help      Display this help text
"
}

case $1 in
    flask|nginx)      NORMAL_CONTAINER=1 ;;
    database)         DATABASE_CONTAINER=1 ;;
    help|*)           usage; exit 1 ;;
esac

if [ -n "$NORMAL_CONTAINER" ]; then
    docker-compose exec "${1}" /bin/bash
fi

if [ -n "$DATABASE_CONTAINER" ]; then
    docker-compose exec database gosu postgres psql -d city_owned_property
fi
