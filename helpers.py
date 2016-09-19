import math

from colors import beautiful_print, Colors


def chunks(data, max_chunk_size):
    num_of_chunks = str(int(math.ceil(float(len(data)) / max_chunk_size)))
    beautiful_print(Colors.OKBLUE, 'Breaking users in ' + num_of_chunks + ' chunks.')

    return [data[i:i + max_chunk_size] for i in range(0, len(data), max_chunk_size)]
