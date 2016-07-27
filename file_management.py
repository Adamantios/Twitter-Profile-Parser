import json

import unicodecsv


class FileManagement:
    """Makes all the appropriate management of the files."""

    def __init__(self):
        pass

    @staticmethod
    def load_file(filename):
        with open(filename, 'r') as f:
            data = []

            for line in f:
                data.append(line.strip().split(' '))

        return data

    @staticmethod
    def write_data_to_file(data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f)
