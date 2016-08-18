#!/bin/bash

set -ex

usage="$(basename "$0") [-h] [-c]
--Sets up a postgresql database

where:
    -h  show this help text
    -c  add city_owned_property table
"

while getopts ":hc" opt; do
    case $opt in
        h)
            echo -e $usage
            exit ;;
        c)
            add_city_owned_property_table=true ;;
        \?)
            echo "invalid option: -$OPTARG"
            exit ;;
    esac
done

if [ "$add_city_owned_property_table" = "true" ] ; then
    cat ./scripts/database/create_city_owned_properties.sql | \
    docker exec -i vagrant_database_1 gosu postgres psql -d city_owned_property
fi
