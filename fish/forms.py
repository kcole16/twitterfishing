from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm

from datetime import datetime


class TweetForm(forms.Form):
    tweet = forms.CharField(max_length = 140)
    target_language = forms.CharField(label='Choose Language:',widget=forms.RadioSelect( choices=(
        ('en', 'English'),
        ('es', 'Spanish'),
        ('de', 'German'),
        ('fr', 'French'),
        ('ru', 'Russian'),
        ('ar', 'Arabic'),
        ('it', 'Italian'),
        ('pt', 'Portuguese')
        )))

