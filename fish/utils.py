from django.contrib.auth.models import User

from social.apps.django_app.default.models import *

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
	
	status = api.post_translations(text=str(tweet),target_language=target_lang, callback_url='http://twitterfishing.herokuapp.com/fish/handle_translation/')

	uid = status.uid

	return uid

	
def send_tweet(user_id, text):
	user = User.objects.get(id=user_id)
	data = UserSocialAuth.objects.get(user_id=user.id).extra_data
	access_key = data['access_token']['oauth_token']
	access_secret = data['access_token']['oauth_token_secret']

	api = twitter.Api(consumer_key=TWITTER_KEY,consumer_secret=TWITTER_SECRET,access_token_key=access_key,access_token_secret=access_secret)

	status = api.PostUpdate(text)
	print status.text

