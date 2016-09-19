import json
from os import makedirs, path

from colors import beautiful_print, Colors


def load_file(filename):
    with open(filename, 'r') as f:
        data = []

        for line in f:
            data.append(line.strip().split(' '))

    if len(data) == 0:
        beautiful_print(Colors.WARNING, 'The input file is empty!')
        exit(1)

    return data


def write_data_to_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


def create_results_folder():
    if not path.exists('results'):
        makedirs('results')


def create_result_file(results, name, counter):
    create_results_folder()
    write_data_to_file(results, 'results/' + name + '.json')
    beautiful_print(Colors.OKGREEN, str(counter) + ': Profile data for user ' + name + ' have been written in \'' \
        + name + '.json\', in \'results\' folder.')
