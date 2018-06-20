# Twitter-Profile-Parser
A twitter profile parser, which returns specific data of twitter users.
Written in Python 2.7

## Input
The twitter profile parser takes as an input a csv or line separated file containing the twitter screen names of the users
for whom we want to download the specific data.

### NOTES:
-In order to change the downloaded data, just change the `get_specific_user_data(user)` function.  
-After every chunk downloaded, if any user could not be fetched, shows a message specifying the username(s) converted in lower case.

## Requirements
tweepy is required.

## Usage
```
twitter_profile_parser.py [-h]  -f FILENAME 
                                [-s STATUSES] [-q MAX_QUERY_SIZE]
                                [-t MINUTES_TO_SLEEP]

required arguments:
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

## Results
Creates `json` files with all the downloaded users' data in a folder *results*.  
After every chunk downloaded, if any user could not be fetched, shows a message specifying the username(s) converted in lower case.  
If any user's tweets could not be fetched, shows warning message.

## Example
### users.txt file contents:
BarackObama
ThisIsHereInOrderToDemonstrateWhatHappensIfANameDoesntExist
YouTube
twitter
cnnbrk
instagram
shakira

### Executed command:
twitter_profile_parser.py -f input/users.txt -s 5

### Console output(colorful in Linux):
```
Breaking users in 1 chunks.
Trying to fetch 7 users...

1: User BarackObama was fetched!
[{u'message': u'User not found.', u'code': 50}]
2: User with screen name: ThisIsHereInOrderToDemonstrateWhatHappensIfANameDoesntExist could not be fetched!
3: User YouTube was fetched!
4: User twitter was fetched!
5: User cnnbrk was fetched!
6: User instagram was fetched!
7: User shakira was fetched!

Fetched 6 users out of 7.

1: Profile data for user BarackObama have been written in 'BarackObama.json', in 'results' folder.
2: Profile data for user YouTube have been written in 'YouTube.json', in 'results' folder.
3: Profile data for user twitter have been written in 'twitter.json', in 'results' folder.
4: Profile data for user cnnbrk have been written in 'cnnbrk.json', in 'results' folder.
5: Profile data for user instagram have been written in 'instagram.json', in 'results' folder.
6: Profile data for user shakira have been written in 'shakira.json', in 'results' folder.
The following user(s) could not be fetched:
['thisishereinordertodemonstratewhathappensifanamedoesntexist']
The non fetched names shown, have been converted to lowercase!
The searching process is case insensitive!
```

### Json Result Files' Contents:
```
{
  "BarackObama": {
    "user_listed": 215436,
    "user_followers": 77150422,
    "user_favs": 10,
    "user_statuses": 15247,
    "user_friends": 634455,
    "user_tweets": [
      "Senate leaders have 32 days before their next recess to give Judge Garland a hearing and a vote. Call them out now: https://t.co/IV1AGOEDag",
      "The Paris Climate Agreement is a big deal in the fight against climate change\u2014and now, a big step closer to reality. https://t.co/5vd6n0BFgG",
      "The United States is leading the way in the fight to #ActOnClimate. https://t.co/vkUMjg6XKc",
      "Conservation not only protects diverse lands and species, it's also an important part of battling climate change. https://t.co/gjvhHNPFKL",
      "\"When we protect our lands, it helps us protect the climate for the future.\" \u2014President Obama #ActOnClimate https://t.co/qdoCgYPQom"
    ],
    "user_verified": true
  }
}
```

```
{
  "cnnbrk": {
    "user_listed": 176242,
    "user_followers": 41822343,
    "user_favs": 18,
    "user_statuses": 50974,
    "user_friends": 119,
    "user_tweets": [
      "RT @CNNent: Donald Trump's media blacklist is officially over as of Thursday. https://t.co/tXpoQ7lPXM by @brianstelter https://t.co/VnRgV9u\u2026",
      "RT @CNNMoney: U.S. stocks start with small losses. Dow off 25 points. Chipotle rises 5%, a day after Bill Ackman buys big stake. https://t.\u2026",
      "RT @CNNMoney: .@Starbucks CEO Howard Schultz endorses @HillaryClinton during CNNMoney Facebook Live https://t.co/np01zPsLjq https://t.co/SM\u2026",
      "Joe Hosteen Kellwood, one of the Navajo code talkers during World War II, has died at age 95. https://t.co/AiMKpFjdxO",
      "4 dead after criminals downed an aircraft in southwestern Mexico, state governor says https://t.co/hQBcGgBHGr https://t.co/pJKx1PD2v4"
    ],
    "user_verified": true
  }
}
```

```
{
  "instagram": {
    "user_listed": 33137,
    "user_followers": 40475184,
    "user_favs": 101,
    "user_statuses": 9263,
    "user_friends": 4,
    "user_tweets": [
      "A foggy jog through San Francisco\u2019s Mount Davidson Park https://t.co/EFOD7ZS3yN",
      "#DailyFluff\nhttps://t.co/OgFjORnXzr \ud83d\udc3e https://t.co/sSuaTEbDgj",
      "A burst of energy and light erupts in a forest clearing \ud83d\udca5 #WHPwilderness https://t.co/owO0wbGqy8",
      "Featured submissions from this weekend\u2019s hashtag project: #WHPwilderness https://t.co/5oUkSgmSZb https://t.co/w0geEf5RRk",
      "RT @InstagramMusic: .@kanyewest on an ultralight beam #weekendmusic https://t.co/0Xbx71DGgM"
    ],
    "user_verified": true
  }
}
```

```
{
  "shakira": {
    "user_listed": 102195,
    "user_followers": 39756526,
    "user_favs": 411,
    "user_statuses": 4192,
    "user_friends": 183,
    "user_tweets": [
      "Gracias a todos por sus  mensajes de cari\u00f1o y buenos deseos para mi papa en su cumple!! Muah! Shak https://t.co/6Roy2R0pUH",
      "Feliz 85avo cumplea\u00f1os papi!! Shak https://t.co/r7Vw5oPFmh",
      "Wait, let's hear that again...Shak https://t.co/nYWwrjN0y2",
      "Video: Fundaci\u00f3n Brindemos Sonrisas on instagram #LaBicicletaKids \ud83d\udeb2 ShakHQ @carlosvives https://t.co/RxJEWW8ThF",
      "So pleased to report that the #ALASIDBAwards received 1101 proposals from 20 LATAM countries @MorenoBID ShakHQ"
    ],
    "user_verified": true
  }
}
```

```
{
  "twitter": {
    "user_listed": 90395,
    "user_followers": 56596869,
    "user_favs": 2059,
    "user_statuses": 3123,
    "user_friends": 145,
    "user_tweets": [
      "This #TravelTuesday, see why Mark Twain once wrote, \"heaven was copied after Mauritius.\"\n\ud83c\udf34 https://t.co/2HJS8xhBqe https://t.co/gjHtHikxfK",
      "@Nah_shelly Happy birthday, Nashelly! Here's another \ud83c\udf88",
      "We \ud83d\udc40 you, Jupiter. #JunoMission \nhttps://t.co/YphJMZhTo0",
      "RT @gov: Tracking #Hermine this Labor Day weekend? Follow this list for live updates: https://t.co/kjRnzsiyO3 #FollowFriday https://t.co/DI\u2026",
      "Summer's almost over. What's your #FridayFeeling?"
    ],
    "user_verified": true
  }
}
```

```
{
  "YouTube": {
    "user_listed": 80356,
    "user_followers": 63860528,
    "user_favs": 1382,
    "user_statuses": 17407,
    "user_friends": 945,
    "user_tweets": [
      "They can make you go back to school, but they\u2019ll never take your style. https://t.co/kRRvw59xfB https://t.co/zqsLvhW1s2",
      "Always stoked to see YouTubers on TV. Congrats, @SimoneGiertz \ud83d\udc4f \ud83d\udc4f \ud83d\udc4f https://t.co/q0Y4xa09Ui https://t.co/H6i9PhlPdD",
      "@AmkcccAndy So good! Those eyes are so blue ... so Bunny!",
      "We\u2019ve seen you again \u2026 over 2 billion times. Congratulations @wizkhalifa and @charlieputh. https://t.co/Fo1aWNjD7w https://t.co/NyvrZXSyzh",
      "RT @AURORAmusic: Excited for my Fall N. America Tour! Warriors+Weirdos: Get tix at 10am tmrw: PW=WENTTOOFAR https://t.co/Er5kZBrmX1 https:/\u2026"
    ],
    "user_verified": true
  }
}
```
