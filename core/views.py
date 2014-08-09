from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render_to_response, render, redirect
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db import IntegrityError, connection, transaction
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from finished.models import Item

def home(request):
	no_items = False
	try:
		item_queryset=Item.objects.order_by('id')

	except ObjectDoesNotExist:
		no_items = True
		return render_to_response('core/home.html',{'items':items, 'no_items':no_items}, context_instance=RequestContext(request))
	else:
		items_unordered = [item.content for item in item_queryset]
		items = items_unordered[-5:]
		return render_to_response('core/home.html',{'items':items}, context_instance=RequestContext(request))


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
