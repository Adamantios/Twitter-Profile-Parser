from argparse import ArgumentParser
from itertools import chain
from os import makedirs
from os import path
from time import sleep

from tweepy import API
from tweepy import OAuthHandler
from tweepy import TweepError

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


def get_twitter_api():
    auth = OAuthHandler(args.consumer_key, args.consumer_secret)
    auth.set_access_token(args.access_token, args.access_token_secret)
    return API(auth)


def chunks(data, max_chunk_size):
    return [data[i:i + max_chunk_size] for i in range(0, len(data), max_chunk_size)]


def get_specific_user_data(user):
    statuses = api.user_timeline(user.screen_name, count=args.statuses)
    tweets = list(status.text for status in statuses)

    return {'user_followers': user.followers_count,
            'user_listed': user.listed_count,
            'user_verified': user.verified,
            'user_statuses': user.statuses_count,
            'user_friends': user.friends_count,
            'user_favs': user.favourites_count,
            'user_tweets': tweets}


def create_results_folder():
    if not path.exists('results'):
        makedirs('results')


def create_result_file(results, name, counter):
    create_results_folder()
    FileManagement.write_data_to_file(results, 'results/' + name + '.json')
    print str(counter) + ': The downloaded profile data have been written in \'' \
          + name + '.json\', in \'results\' folder.'


def fetch_data():
    need_to_sleep = False
    user_data = {}
    user_counter = 0

    for chunk in users_chunks:

        if need_to_sleep:
            print 'Sleeping for ' + str(args.minutes_to_sleep) + ' minute(s)...'
            sleep(60 * args.minutes_to_sleep)

        chunk = list(chain.from_iterable(chunk))

        try:
            users = api.lookup_users(screen_names=chunk)
            expected = str(len(chunk))
            found = str(len(users))
            print 'Fetching ' + found + ' users out of ' + expected + '.'
            chunk = list(set(i.lower() for i in chunk))

            for u in users:
                user_counter += 1
                chunk.remove(str(u.screen_name).lower())
                user_data[u.screen_name] = get_specific_user_data(u)
                create_result_file(user_data, u.screen_name, user_counter)
                user_data.clear()

            if found < expected:
                print '\nThe following user(s) do not exist:\n' + str(chunk)
                print '\nNOTE: The non existing names shown, have been converted to lowercase!\n' \
                      'The searching process is case insensitive, ' \
                      'so you can safely remove them without trying to capitalise certain letters ' \
                      'and use them again!'

            need_to_sleep = True

        except TweepError:
            print 'The following user(s) do not exist:\n' + str(chunk)


def main():
    # noinspection PyGlobalUndefined
    global args, api, users_chunks
    args = parse_arguments()
    api = get_twitter_api()
    usernames = FileManagement.load_file(args.filename)
    users_chunks = chunks(usernames, args.max_query_size)
    fetch_data()


if __name__ == "__main__":
    main()
