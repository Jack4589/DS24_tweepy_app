import tweepy

# API KEYS
API_KEY = "cwKPyekTUT2Bl3WKdz3aN3Xyy"  # "Username"
API_KEY_SECRET = "QengYRcqgB3m2Or5SGaaDuP5Ph6cNvTTCdlVqlrtGWmaHfxF7U"  # "Password"

# Authentication and passing in keys
auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
twitter = tweepy.API(auth)

# defining variable to pass into get_user
username = "elonmusk"

# getting twitter user from Twitter DB
twitter_user = twitter.get_user(username)
# twitter_user.id, twitter_user.name, twitter_user.created_at

# returns list of tweets
tweets = twitter_user.timeline(
    count=200,
    exclude_replies=True,  # optional
    include_rts=False,  # optional
    tweet_mode="Extended"  # optional - specifies that we want unicode
)
# i == indexing list
# get tweet text == tweets[i].text
# get created at == tweets[i].created_at
# associated user == tweets[i].user
