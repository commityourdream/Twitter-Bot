import tweepy
import time

auth = tweepy.OAuthHandler('API key:', 'API key secret:')

auth.set_access_token('Access token:', 'Access token secret:')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = '100DaysOfCode '
nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(10)
        tweet.retweet()
        print('tweet got retwitted')

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break





'''
for follower in tweepy.Cursor(api.followers).items():
    if follower.name == 'traversy media':
'''
