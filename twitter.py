from os import getenv
import tweepy

auth = tweepy.OAuthHandler("cwKPyekTUT2Bl3WKdz3aN3Xyy",
                           "QengYRcqgB3m2Or5SGaaDuP5Ph6cNvTTCdlVqlrtGWmaHfxF7U")
twitter = tweepy.API(auth)


def get_info(username):
    try:
        twitter_user = twitter.get_user(username)
        tweets = twitter_user.timeline(
            count=500,
            exclude_replies=True,
            include_rts=False
        )
        tweets_text = []
        for tweet in tweets:
            tweets_text.append(tweet)

        return twitter_user, tweets_text

    except Exception as e:
        print("Error Processing %s: %s" % (username, e))
