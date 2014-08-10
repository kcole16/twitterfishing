from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, render, redirect
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.db import IntegrityError, connection, transaction
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse

from finished.models import Item
from core.models import Account
from core.forms import AccountForm

import json
import requests

@login_required
def home(request):
	no_items = False
	try:
		# item_queryset=Item.objects.order_by('id')
		items = Item.objects.all()
	except ObjectDoesNotExist:
		no_items = True
		return render_to_response('core/home.html',{'items':items, 'no_items':no_items}, context_instance=RequestContext(request))
	else:
		# items_unordered = [item.content for item in item_queryset]
		# items = items_unordered[-5:]
		return render_to_response('core/home.html',{'items':items}, context_instance=RequestContext(request))


def handle_yoauth(request):
	yoauth_token = request.GET['yoauth_token']
	url = 'http://yoauth.herokuapp.com/validate'
	payload = {'yoauth_token':yoauth_token}
	r = requests.get(url, params=payload)
	text = json.loads(r.text)
	username = str(text['user']['yo_username'])

	try:
		user = Account.objects.get(yo_name=username)
	except ObjectDoesNotExist:
		user = Account(yo_name=username, password='!')
		user.save()

	user.backend = 'django.contrib.auth.backends.ModelBackend'
	login(request, user)
	url = reverse('home')
	return HttpResponseRedirect(url)


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


def create_account(request):
	if request.POST:
		form = AccountForm(request.POST)
		if form.is_valid():
			form.save()
			user = Account.objects.get(id=form.instance.id)
			pw = user.password
			user.set_password(pw)
			user.save()
			url = reverse('home')
			return HttpResponseRedirect(url) 
		else:
			print form.errors
	else:
		form = AccountForm()
	
	return render_to_response('core/create_account.html', context_instance=RequestContext(request))

