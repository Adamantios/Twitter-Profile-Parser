from api_communication import get_twitter_api, fetch_data
from argument_parser import parse_arguments

from file_management import load_file
from helpers import chunks


def main():
    args = parse_arguments()
    api = get_twitter_api()
    usernames = load_file(args.filename)
    users_chunks = chunks(usernames, args.max_query_size)
    fetch_data(users_chunks, args.minutes_to_sleep, api, args.statuses)


if __name__ == "__main__":
    main()
