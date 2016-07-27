# Twitter-Profile-Parser
A twitter profile parser, which returns specific data of twitter users.
Written in Python 2.7

##Input
The twitter profile parser gets all the required twitter authentication keys as input
and a csv or line separated file containing the twitter screen names of the users
for whom we want to download the specific data.

###NOTE:
In order to change the downloaded data, just change the `get_specific_user_data(user)` function.

##Requirements
tweepy is required.

##Usage
```
twitter_profile_parser.py [-h] -ck CONSUMER_KEY -cs CONSUMER_SECRET -at
                                ACCESS_TOKEN -ats ACCESS_TOKEN_SECRET -f
                                FILENAME [-q MAX_QUERY_SIZE]
                                [-t MINUTES_TO_SLEEP]

required arguments:
  -ck CONSUMER_KEY, --consumerkey CONSUMER_KEY
                        The consumer key for the authentication.
                        
  -cs CONSUMER_SECRET, --consumersecret CONSUMER_SECRET
                        The consumer secret for the authentication.
                        
  -at ACCESS_TOKEN, --accesstoken ACCESS_TOKEN
                        The access token for the authentication.
                        
  -ats ACCESS_TOKEN_SECRET, --accesstokensecret ACCESS_TOKEN_SECRET
                        The access token secret for the authentication.
                        
  -f FILENAME, --file FILENAME
                        path to the file which contains the twitter usernames.


optional arguments:
  -h, --help            shows a help message and exits.
  
  -q MAX_QUERY_SIZE, --querysize MAX_QUERY_SIZE
                        The number of queries to be executed before sleeping
                        for some minutes.The default value is 180, the current
                        twitter's maximum requests allowed.
                        
  -t MINUTES_TO_SLEEP, --time MINUTES_TO_SLEEP
                        The sleeping time between the queries in minutes.The
                        default value is 15, the current twitter's minimum
                        time of waiting between the requests.
  ```

##Results
Creates a `json` file with all the downloaded users' data in a folder *results*.
If something goes wrong, creates a file with the partly downloaded data.

##Example
###users.txt file contents:
BarackObama
YouTube
twitter
cnnbrk
instagram
shakira

###Executed command:
twitter_profile_parser.py -ck xxx -cs xxx -at xxx -ats xxx -f input/users.txt

###Json Result File Contents:
```
{
  "instagram": {
    "user_listed": 32981,
    "user_followers": 40600213,
    "user_favs": 99,
    "user_statuses": 8863,
    "user_friends": 4,
    "user_verified": true
  },
  "YouTube": {
    "user_listed": 80202,
    "user_followers": 63160600,
    "user_favs": 1360,
    "user_statuses": 17103,
    "user_friends": 930,
    "user_verified": true
  },
  "twitter": {
    "user_listed": 90267,
    "user_followers": 55978508,
    "user_favs": 1819,
    "user_statuses": 3010,
    "user_friends": 145,
    "user_verified": true
  },
  "cnnbrk": {
    "user_listed": 175587,
    "user_followers": 40733122,
    "user_favs": 18,
    "user_statuses": 50275,
    "user_friends": 120,
    "user_verified": true
  },
  "shakira": {
    "user_listed": 102231,
    "user_followers": 38964449,
    "user_favs": 379,
    "user_statuses": 4100,
    "user_friends": 180,
    "user_verified": true
  },
  "BarackObama": {
    "user_listed": 215329,
    "user_followers": 76293559,
    "user_favs": 10,
    "user_statuses": 15116,
    "user_friends": 635147,
    "user_verified": true
  }
}
```
