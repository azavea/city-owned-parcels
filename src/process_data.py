#!/usr/bin/env python

import os
import sys
import csv

ID_INDEX = 47
DISTINCT = 'distinct'
DIFF = 'diff'
ADD = 'add'
REMOVE = 'remove'

def load_csv_set(csv_filename):
    with open(csv_filename, 'rb') as csv_file:
        csv_set = set()
        csv_reader = csv.reader(csv_file)

        header = tuple(next(csv_reader, None))
        for csv_row in csv_reader:
            csv_set.add(tuple(csv_row))

        return header, csv_set


def write_csv_set(csv_filename, header, csv_set):
    with open(csv_filename, 'wb') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(header)
        for row in csv_set:
            csv_writer.writerow(row)


def get_id_set(csv_set):
    return set(map(lambda row: row[ID_INDEX], csv_set))


def get_rows_with_ids(csv_set, ids):
    csv_dict = dict(map(lambda row: (row[ID_INDEX], row), csv_set))
    return map(lambda id: csv_dict[id], ids)


def make_filename(root, tag, extension):
    return '{0}_{1}{2}'.format(root, tag, extension)


def get_diff(old_set, new_set):
    old_ids = get_id_set(old_set)
    new_ids = get_id_set(new_set)

    add_ids = new_ids - old_ids
    add_rows = get_rows_with_ids(new_set, add_ids)

    remove_ids = old_ids - new_ids
    remove_rows = get_rows_with_ids(old_set, remove_ids)

    return add_rows, remove_rows


def augment_rows(csv_set, append_val):
    return map(lambda row: [append_val] + list(row), csv_set)


def process_data(old_filename, new_filename):
    new_filename_root, new_filename_ext = os.path.splitext(new_filename)
    def make_new_filename(tag):
        return make_filename(new_filename_root, tag, new_filename_ext)
    new_distinct_filename = make_new_filename(DISTINCT)
    new_diff_filename = make_new_filename(DIFF)

    header, old_set = load_csv_set(old_filename)
    _, new_set = load_csv_set(new_filename)

    write_csv_set(new_distinct_filename, header, new_set)

    add_rows, remove_rows = get_diff(old_set, new_set)
    add_rows = augment_rows(add_rows, ADD)
    remove_rows = augment_rows(remove_rows, REMOVE)

    diff_header = [DIFF] + list(header)
    diff_rows = add_rows + remove_rows

    write_csv_set(new_diff_filename, diff_header, diff_rows)


def run_test():
    # old.txt has two rows with ids 1 and 2
    old_filename = 'test_data/old.txt'
    # new.txt has three rows with ids 1, 1, and 3
    new_filename = 'test_data/new.txt'
    process_data(old_filename, new_filename)

    # distinct.txt should contain two rows with ids 1 and 3
    _, new_distinct_set = load_csv_set('test_data/new_distinct.txt')
    assert(len(new_distinct_set) == 2)
    assert(len(get_id_set(new_distinct_set).intersection(set(['1', '3']))) == 2)

    # diff.txt should contain two rows with remove 2 and add 3
    _, new_diff_set = load_csv_set('test_data/new_diff.txt')
    new_diff_set = set(map(lambda row: (row[0], row[ID_INDEX+1]), new_diff_set))
    assert(len(new_diff_set) == 2)
    assert((REMOVE, '2') in new_diff_set)
    assert((ADD, '3') in new_diff_set)


def main():
    run_test()

if __name__ == '__main__':
    main()
