from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, render, redirect
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db import IntegrityError, connection, transaction
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse

from core.models import Account
from finished.models import Item
from finished.forms import ItemForm

from datetime import datetime


# def create_account(request):
# 	if request.POST:
# 		form = AccountForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			user_id = form.instance.id
# 			password = Account.objects.get(id=user_id)
# 			pw = password.password
# 			check=password.email.split("@")
# 			password.set_password(pw)
# 			password.save()		
# 			if check[1]!="virginia.edu":
# 				Account.objects.filter(id=user_id).delete()	
# 				return render_to_response('around/email_fail.html',context_instance=RequestContext(request))
# 			else:
# 				return HttpResponseRedirect('/around/home') 
# 		else:
# 			print form.errors
# 	else:
# 		form = AccountForm()
	
# 	return render_to_response('around/create_account.html', context_instance=RequestContext(request))


def add_item(request):
	user = Account.objects.get(id=1)
	if request.POST:
		form = ItemForm(request.POST)
		#user = Account.objects.get(id=request.user.id)
		form.is_valid()
		print form.cleaned_data
		content_to_use = form.cleaned_data['content']
		new_item = Item(content=content_to_use, user=user)
		new_item.save()

		url = reverse('home')
		return HttpResponseRedirect(url) 
	else:
		return render_to_response('finished/add_item.html', context_instance=RequestContext(request))


def handle(request):
	print request.GET

def delete_item(request,item_id):
	item_to_delete = Item.objects.get(id=item_id)
	item_to_delete.delete()

	url = reverse('home')
	return HttpResponseRedirect(url) 



