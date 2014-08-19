from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm

from datetime import datetime

from core.models import Account, AccountManager

class TwitterForm(forms.Form):
    handle = forms.CharField(max_length = 1024)
    target_language = forms.CharField(label='Choose Language:',widget=forms.RadioSelect(attrs={ 'class': 'categories' }, choices=(
        ('en', 'English'),
        ('es', 'Spanish'),
        ('de', 'German'),
        ('fr', 'French'),
        ('ru', 'Russian'),
        ('ar', 'Arabic'),
        ('it', 'Italian'),
        ('pt', 'Portuguese')
        )))

