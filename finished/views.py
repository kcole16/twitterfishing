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
from finished.models import Item
from finished.forms import ItemForm

from datetime import datetime


def add_item(request):
	print request.user.id
	user = Account.objects.get(id=request.user.id)
	if request.POST:
		form = ItemForm(request.POST)
		form.is_valid()
		print form.cleaned_data
		content_to_use = form.cleaned_data['content']
		new_item = Item(content=content_to_use, user=user)
		new_item.save()

		url = reverse('home')
		return HttpResponseRedirect(url) 
	else:
		return render_to_response('finished/add_item.html', context_instance=RequestContext(request))


def handle(request, username):
	username = request.GET['username']
	user = Account.objects.get(yo_name=str(username))
	item_to_delete = Item.objects.filter(user_id=user.id).earliest('date_created')
	item_to_delete.delete()
	url = reverse('home')
	return HttpResponseRedirect(url) 


def delete_item(request,item_id):
	item_to_delete = Item.objects.get(id=item_id)
	item_to_delete.delete()

	url = reverse('home')
	return HttpResponseRedirect(url) 



