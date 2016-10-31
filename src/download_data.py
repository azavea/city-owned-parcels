import requests

ALIAS_FILENAME = 'phila_aliases.txt'
URL_ROOT = 'https://data.phila.gov/resource/tqtk-pmbv.csv'
URL_PATTERN = '{URL_ROOT}?$limit=50000&$order=parcel_number&owner_1={alias}'

def download_data(data_filename):
    with open(ALIAS_FILENAME) as aliases, \
         open(data_filename, 'w') as data_file:
        for alias_ind, alias in enumerate(aliases):
            if alias != '\n':
                alias = alias.strip()
                url = URL_PATTERN.format(URL_ROOT=URL_ROOT, alias=alias)
                print(url)

                r = requests.get(url)
                for line_ind, line in enumerate(r.iter_lines()):
                    # Only write header for first URL
                    if line and (alias_ind == 0 or line_ind > 0):
                        data_file.write(line + '\n')


def main():
    data_filename = 'test_data/download.txt'
    download_data(data_filename)

if __name__ == '__main__':
    main()
