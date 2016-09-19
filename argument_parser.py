from argparse import ArgumentParser


# noinspection SpellCheckingInspection
def parse_arguments():
    parser = ArgumentParser(description='Get specific user data from twitter.')

    parser.add_argument('-f', '--file', type=str,
                        required=True, dest='filename',
                        help='path to the file which contains the twitter usernames.')
    parser.add_argument('-s', '--statuses', type=int,
                        dest='statuses', default=100,
                        help='The number of the most recent tweets to fetch for each user.'
                             'The default value is 100.')
    parser.add_argument('-q', '--querysize', type=int,
                        dest='max_query_size', default=180,
                        help='The number of queries to be executed before sleeping for some minutes.'
                             'The default value is 180, the current twitter\'s maximum requests allowed.')
    parser.add_argument('-t', '--time', type=int,
                        dest='minutes_to_sleep', default=15,
                        help='The sleeping time between the queries in minutes.'
                             'The default value is 15, the current twitter\'s minimum time of waiting'
                             ' between the requests.')

    return parser.parse_args()
