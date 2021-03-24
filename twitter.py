from os import getenv
import tweepy

auth = tweepy.OAuthHandler("NMV0tKMlshhMYTzqwh44CjPzV",
                           "QhLLsomQrqvfGiPb8pCemrKND7izBWLf2Vkuzf1xTjA1pzsFtu")
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
