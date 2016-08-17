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
twitter_profile_parser.py [-h] -ck CONSUMER_KEY -cs CONSUMER_SECRET 
                                -at ACCESS_TOKEN -ats ACCESS_TOKEN_SECRET 
                                -f FILENAME 
                                [-s STATUSES] [-q MAX_QUERY_SIZE]
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
  
  -s STATUSES, --statuses STATUSES
                        The number of the most recent tweets to fetch for each
                        user.The default value is 100.
                        
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
twitter_profile_parser.py -ck xxx -cs xxx -at xxx -ats xxx -f input/users.txt -s 5

###Json Result File Contents:
```
{
  "instagram": {
    "user_listed": 33065,
    "user_followers": 40560857,
    "user_favs": 101,
    "user_statuses": 9066,
    "user_friends": 4,
    "user_tweets": [
      "A symbiotic submission to last weekend\u2019s hashtag project, #WHPsymmetry https://t.co/GN4CAYuHmi",
      "RT @Terr: thank you @tavitulle for taking over our Instagram Story today i am literally obsessed with your Teen Vogue cover https://t.co/em\u2026",
      "RT @umamiburger: Follow us on @instagram to get the first look at our exclusive burger in Pasadena! #instagramstories https://t.co/GB2Onx2O\u2026",
      "RT @alternahaircare: Check out our Instagram story for a Q &amp; A with @KatieHolmes212! https://t.co/EBjW65pqhT https://t.co/xBbQ7QkZv4",
      "RT @tavitulle: I took over @TeenVogue's instagram story today \ud83d\ude08 https://t.co/8DbJtksTDd"
    ],
    "user_verified": true
  },
  "YouTube": {
    "user_listed": 80264,
    "user_followers": 63532620,
    "user_favs": 1375,
    "user_statuses": 17258,
    "user_friends": 933,
    "user_tweets": [
      "When you look in the mirror and realize you've turned into a terrifying squid. https://t.co/KPf7HgvXMT #squidgoals https://t.co/zhBLPzejhB",
      "@Iam_Hyem Now that is the boat to be on.",
      "@KickinMajorFlav So ready. Especially in that hat. #FOTLD",
      "@dddddanniell It'll totally help. Especially the hat. Definitely the hat. #FOTLD",
      "@kayla_dishner YES. Did you like what you found inside? #FOTLD"
    ],
    "user_verified": true
  },
  "twitter": {
    "user_listed": 90303,
    "user_followers": 56328152,
    "user_favs": 2015,
    "user_statuses": 3081,
    "user_friends": 145,
    "user_tweets": [
      "Close out #TravelTuesday with a trip to Greece to see Meteora's monasteries in the sky: https://t.co/lKxxygnvx2 https://t.co/pGAT3L2wnk",
      "Pass the remote! After reading your #7FavTVShows, we've got a lot to watch. \ud83d\udcfa https://t.co/sS6lmvjTCH https://t.co/NtFojoqWUW",
      "Your favorite events, right in your timeline! Follow a Moment for live updates from #Rio2016 https://t.co/mBvPYxMt1l https://t.co/HvlEeAaGnn",
      "See what's happening \u2014 politics on Twitter.\nhttps://t.co/3KWjYe3jb9",
      "First-time champions, repeat winners, and lightning on the track \u2014 see what happened this weekend at #Rio2016.\nhttps://t.co/x4sMTYTyyX"
    ],
    "user_verified": true
  },
  "cnnbrk": {
    "user_listed": 175875,
    "user_followers": 41305587,
    "user_favs": 18,
    "user_statuses": 50676,
    "user_friends": 119,
    "user_tweets": [
      "Donald Trump's campaign is undergoing a major staff shakeup, adding two officials to top posts. https://t.co/P3cmmmTG4e",
      "Malaysian oil tanker carrying about $400K worth of diesel was hijacked, taken to Indonesian waters, authorities say. https://t.co/WtiV55Ud9X",
      "Jalisco attorney general: Joaquin \u2018El Chapo\u2019 Guzman\u2019s son was among those kidnapped in Puerto Vallarta. https://t.co/riJSJH5cA0",
      "John McLaughlin, the host of \u2018The McLaughlin Group\u2019 show, dies at 89. https://t.co/AxH1dgs2Pd https://t.co/I6lrxPEFcE",
      "RT @CNNMoney: Stocks end lower. Dow falls 84 points, Nasdaq off 0.7%. Oil continues to creep upward, comfortably over $46/barrel. https://t\u2026"
    ],
    "user_verified": true
  },
  "shakira": {
    "user_listed": 102231,
    "user_followers": 39378392,
    "user_favs": 398,
    "user_statuses": 4160,
    "user_friends": 183,
    "user_tweets": [
      "RT @carlosvives: #labicicletakids @clarapablo que espect\u00e1culo te quiero abrazos!!! @shakira \n#Repost @clarapablo\u2026 https://t.co/cA1wWHTNd9",
      "RT @shakifan2277: @shakira @carlosvives #LaBicicletaKids  Mi bailarin bello\ud83d\udc97 Te amo Shakira https://t.co/D8pWq4W0tC",
      "\"Shakira Shares Adorable Videos of Kids Dancing to Her Song La Bicicleta\" @enews #LaBicicletaKids ShakHQ   https://t.co/gadgoZ53HL",
      "Video: @jackiee80 on Instagram #LaBicicletaKids \ud83d\udeb2 ShakHQ @carlosvives https://t.co/wfV6kHFA7T",
      "RT @Juancabts: @CarlosVives Isa se sabe todas las canciones de @shakira  y por supuesto #LaBicicletaKids no es la excepci\u00f3n.  \ud83d\ude0d https://t.c\u2026"
    ],
    "user_verified": true
  },
  "BarackObama": {
    "user_listed": 215412,
    "user_followers": 76762669,
    "user_favs": 10,
    "user_statuses": 15188,
    "user_friends": 634813,
    "user_tweets": [
      "RT @WhiteHouse: Here's how today's new actions will spur innovation and promote more efficient vehicles: https://t.co/WoV9454Y4B https://t.\u2026",
      "We\u2019re taking important steps to help guarantee the basic security of paid family leave. https://t.co/yvRhINmIGA #LeadOnLeave",
      "Senate leaders must stop obstructing our Supreme Court. Take a stand and show your support. https://t.co/1AaykUkmvn #DoYourJob",
      "Reminder: It's the Senate's job to fairly consider Supreme Court nominees. #DoYourJob https://t.co/xrkYcRsLNw",
      "Today, thousands of young DREAMers are able to fully contribute to our communities and our economy. https://t.co/szjWDVYm9X"
    ],
    "user_verified": true
  }
}
```
