import datetime
from itertools import chain
from time import time

from tweepy import API
from tweepy import OAuthHandler
from tweepy import TweepError

from colors import beautiful_print, Colors
from counter import countdown
from file_management import create_result_file


# noinspection SpellCheckingInspection
def get_twitter_api():
    consumer_key = '*********************************'
    consumer_secret = '*********************************'
    access_token = '*********************************'
    access_token_secret = '*********************************'

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return API(auth)


def get_users(chunk, counter, api):
    users = []

    for user in chunk:
        counter += 1

        try:
            users.append(api.get_user(user))
            beautiful_print(Colors.OKGREEN, str(counter) + ': User ' + user + ' was fetched!')

        except TweepError, e:
            beautiful_print(Colors.FAIL, str(e.message) +
                            '\n' + str(counter) + ': User with screen name: ' + user + ' could not be fetched!')

    return users


def get_specific_user_data(api, user, statuses):
    try:
        statuses = api.user_timeline(user.screen_name, count=statuses)
        tweets = list(status.text for status in statuses)

        return {'user_followers': user.followers_count,
                'user_listed': user.listed_count,
                'user_verified': user.verified,
                'user_statuses': user.statuses_count,
                'user_friends': user.friends_count,
                'user_favs': user.favourites_count,
                'user_tweets': tweets}, \
            True

    except TweepError, e:
        beautiful_print(Colors.FAIL, str(e.message)
                        + '\nThe tweets of the user: ' + user.screen_name + ' could not be fetched!')

        return {'user_followers': user.followers_count,
                'user_listed': user.listed_count,
                'user_verified': user.verified,
                'user_statuses': user.statuses_count,
                'user_friends': user.friends_count,
                'user_favs': user.favourites_count}, \
            False


def parse_users(users, user_counter, chunk, api, statuses):
    non_fetched = []

    for u in users:
        user_data = {}
        user_counter += 1
        chunk.remove(str(u.screen_name).lower())
        user_data[u.screen_name], status = get_specific_user_data(api, u, statuses)
        create_result_file(user_data, u.screen_name, user_counter)

        if not status:
            non_fetched.append(u.screen_name)

    if len(non_fetched):
        non_fetched.sort()
        beautiful_print(Colors.FAIL, 'The tweets of the following users: '
                        + str(non_fetched) + ' could not be fetched!')

    return chunk, user_counter, time()


def fetch_data(users_chunks, minutes_to_sleep, api, statuses):
    need_to_sleep1 = False
    need_to_sleep2 = False
    user_counter = 0
    time_stopped1 = 0
    time_stopped2 = 0

    for chunk in users_chunks:

        if need_to_sleep1:
            seconds_to_sleep = (datetime.timedelta(minutes=minutes_to_sleep)
                                - datetime.timedelta(seconds=time() - time_stopped1)).total_seconds()

            if seconds_to_sleep > 0:
                m, s = divmod(seconds_to_sleep, 60)
                beautiful_print(Colors.OKBLUE, '\nPausing for ' + str(int(m)) + ' minute(s) and '
                                + str(int(s)) + ' second(s)...\n')
                countdown(int(seconds_to_sleep))

        chunk = list(chain.from_iterable(chunk))

        beautiful_print(Colors.OKBLUE, 'Trying to fetch ' + str(len(chunk)) + ' users...\n')
        users = get_users(chunk, user_counter, api)
        time_stopped1 = time()
        expected = str(len(chunk))
        found = str(len(users))
        beautiful_print(Colors.OKGREEN, '\nFetched ' + found + ' users out of ' + expected + '.\n')
        chunk = list(set(i.lower() for i in chunk))

        if need_to_sleep2:
            seconds_to_sleep = (datetime.timedelta(minutes=minutes_to_sleep)
                                - datetime.timedelta(seconds=time() - time_stopped2)).total_seconds()

            if seconds_to_sleep > 0:
                m, s = divmod(seconds_to_sleep, 60)
                beautiful_print(Colors.OKBLUE, 'Pausing for ' + str(int(m)) + ' minute(s) and '
                                + str(int(s)) + ' second(s)...\n')
                countdown(int(seconds_to_sleep))

        chunk, user_counter, time_stopped2 = parse_users(users, user_counter, chunk, api, statuses)

        if found < expected:
            chunk.sort()
            beautiful_print(Colors.FAIL, 'The following user(s) could not be fetched:\n' + str(chunk))
            beautiful_print(Colors.UNDERLINE, 'The non fetched names shown, have been converted to lowercase!\n'
                                              'The searching process is case insensitive!\n')

        need_to_sleep1, need_to_sleep2 = True, True
