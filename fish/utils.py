from base.settings import *
from unbabel.api import UnbabelApi

import twitter

def get_tweets(user):
	tweets = []
	api = twitter.Api(consumer_key=TWITTER_KEY,
                      consumer_secret=TWITTER_SECRET,
                      access_token_key=ACCESS_KEY,
                      access_token_secret=ACCESS_SECRET)

	statuses = api.GetUserTimeline(screen_name=user)
	for status in statuses:
		tweets.append(status.text)

	return tweets


def translate_tweet(tweet, target_lang):
	api = UnbabelApi(username=UNBABEL_USER,api_key=UNBABEL_KEY,sandbox=True)
	
	status = api.post_translations(text=str(tweet),target_language=target_lang, callback_url='http://twitterfish.herokuapp.com/fish/handle_translation')

	uid = status.uid

	return uid