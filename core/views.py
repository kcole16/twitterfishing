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

from fish.models import Tweet, TwitterHandle
from core.models import Account
from core.forms import AccountForm
from base.settings import *

import json
import requests
import twitter
from unbabel.api import UnbabelApi

def home(request):

	return render_to_response('core/home.html', context_instance=RequestContext(request))

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










