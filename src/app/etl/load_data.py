#!/usr/bin/env python

import os
import sys
import csv

import psycopg2

user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
database = os.environ['POSTGRES_DB']
host = os.environ['POSTGRES_HOST']
port = os.environ['POSTGRES_PORT']

def parse_args():
    if len(sys.argv) == 2:
        csv_file_name = sys.argv[1]
        return csv_file_name
    else:
        return None


def load_data(csv_file_name):
    with open(csv_file_name, 'rb') as csv_file:
        conn = psycopg2.connect(database=database, user=user, password=password,
                                host=host, port=port)
        cursor = conn.cursor()
        placeholders = ', '.join(['%s'] * 77)

        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            row = [val if val != '' else None for val in row]
            query = 'INSERT INTO city_owned_property VALUES ({placeholders})' \
                    .format(placeholders=placeholders)
            cursor.execute(query, row)

        conn.commit()
        cursor.close()
        conn.close()


def main():
    csv_file_name = parse_args()
    if csv_file_name:
        load_data(csv_file_name)
    else:
        print('Expected one argument.')

if __name__ == '__main__':
    main()
