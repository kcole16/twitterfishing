from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, render, redirect
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.db import IntegrityError, connection, transaction
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse

from core.models import Account
from fish.models import Tweet, TwitterHandle
from fish.forms import TwitterForm
from fish.utils import *

from datetime import datetime


def add_handle(request):
	if request.POST:
		form = TwitterForm(request.POST)
		if form.is_valid():
			user = TwitterHandle(handle=form.cleaned_data['handle'])
			user.save()
			raw_tweets = get_tweets(user.handle)
			target_lang = str(form.cleaned_data['target_language'])

			for tweet in raw_tweets:
				uid = translate_tweet(str(tweet), target_lang)
				new_tweet = Tweet(user=user, uid=uid, raw_tweet=str(tweet))
				new_tweet.save()
			return render_to_response('core/home.html', context_instance=RequestContext(request))

	else:
		form = TwitterForm()
	return render_to_response('fish/add_handle.html',{'form':form}, context_instance=RequestContext(request))


def handle_translation(request):
	uid = request.GET['uid']
	tweet_object = Tweet.objects.get(uid=uid)
	tweet_object.translated_tweet = request.GET['translatedText']
	tweet_object.save()
	url = reverse('home')
	return HttpResponseRedirect(url) 



# def delete_item(request,item_id):
# 	item_to_delete = Item.objects.get(id=item_id)
# 	item_to_delete.delete()

# 	url = reverse('home')
# 	return HttpResponseRedirect(url) 



