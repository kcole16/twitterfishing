from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm

from datetime import datetime

from core.models import Account, AccountManager
from finished.models import Item

class ItemForm(forms.Form):
    content = forms.CharField(max_length = 1024)

