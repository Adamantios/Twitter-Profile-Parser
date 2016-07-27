from argparse import ArgumentParser
from tweepy import API
from tweepy import OAuthHandler
from itertools import chain
from time import sleep
from os import path
from os import makedirs
from file_management import FileManagement


# noinspection SpellCheckingInspection
def parse_arguments():
    parser = ArgumentParser(description='Get specific user data from twitter.')
    parser.add_argument('-ck', '--consumerkey', type=str,
                        required=True, dest='consumer_key',
                        help='The consumer key for the authentication.')
    parser.add_argument('-cs', '--consumersecret', type=str,
                        required=True, dest='consumer_secret',
                        help='The consumer secret for the authentication.')
    parser.add_argument('-at', '--accesstoken', type=str,
                        required=True, dest='access_token',
                        help='The access token for the authentication.')
    parser.add_argument('-ats', '--accesstokensecret', type=str,
                        required=True, dest='access_token_secret',
                        help='The access token secret for the authentication.')
    parser.add_argument('-f', '--file', type=str,
                        required=True, dest='filename',
                        help='path to the file which contains the twitter usernames.')
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


def get_twitter_api():
    auth = OAuthHandler(args.consumer_key, args.consumer_secret)
    auth.set_access_token(args.access_token, args.access_token_secret)
    return API(auth)


def chunks(data, max_chunk_size):
    return [data[i:i + max_chunk_size] for i in range(0, len(data), max_chunk_size)]


def get_specific_user_data(user):
    return {'user_followers': user.followers_count,
            'user_listed': user.listed_count,
            'user_verified': user.verified,
            'user_statuses': user.statuses_count,
            'user_friends': user.friends_count,
            'user_favs': user.favourites_count}


def create_results_folder():
    if not path.exists('results'):
        makedirs('results')


def create_result_file(results, succeeded=True):
    if succeeded:
        create_results_folder()
        FileManagement.write_data_to_file(results, 'results/downloaded_profiles.json')
        print 'The downloaded profile data have been written in \'downloaded_profiles.json\'' \
              ', in \'results\' folder.'
    else:
        create_results_folder()
        FileManagement.write_data_to_file(results, 'results/partially_downloaded_profiles.json')
        print 'Some data failed to download!' \
              'The part of the downloaded profile data have been written' \
              ' in \'partially_downloaded_profiles.json\'' \
              ', in \'results\' folder.'


def fetch_data():
    need_to_sleep = False
    users_data = {}

    for chunk in users_chunks:
        try:
            if need_to_sleep:
                print 'Sleeping for ' + str(args.minutes_to_sleep) + ' minute(s)...'
                sleep(60 * args.minutes_to_sleep)

            chunk = list(chain.from_iterable(chunk))
            print 'Fetching ' + str(len(chunk)) + ' users.'
            users = api.lookup_users(screen_names=chunk)

            for u in users:
                users_data[u.screen_name] = get_specific_user_data(u)

            need_to_sleep = True
        except StopIteration:
            create_result_file(users_data, False)

    create_result_file(users_data)


if __name__ == "__main__":
    args = parse_arguments()
    api = get_twitter_api()
    usernames = [username for username in FileManagement.load_file(args.filename)]
    users_chunks = chunks(usernames, args.max_query_size)
    fetch_data()
