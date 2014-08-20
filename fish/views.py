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
from django.contrib.auth.models import User

from fish.models import Tweet
from fish.forms import TweetForm
from fish.utils import *

from datetime import datetime

@login_required
def home(request):

	return render_to_response('core/home.html', context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return redirect('login')

def new_tweet(request):
	user = User.objects.get(id=request.user.id)
	if request.POST:
		form = TweetForm(request.POST)
		if form.is_valid():
			raw_tweet = str(form.cleaned_data['tweet'])	
			target_lang = str(form.cleaned_data['target_language'])
			uid = translate_tweet(raw_tweet, target_lang)

			new_tweet = Tweet(user=user, uid=uid, raw_tweet=raw_tweet)
			new_tweet.save()

			return render_to_response('core/home.html', context_instance=RequestContext(request))

	else:
		form = TweetForm()
	return render_to_response('fish/new_tweet.html',{'form':form}, context_instance=RequestContext(request))

@csrf_exempt
def handle_translation(request):

	uid = request.POST['uid']
	tweet_object = Tweet.objects.get(uid=uid)
	user_id = tweet_object.user_id
	translated_tweet = request.POST['translated_text']

	send_tweet(user_id, translated_tweet)

	tweet_object.translated_tweet = translated_tweet
	tweet_object.save()
	url = reverse('home')
	return HttpResponseRedirect(url) 
 



