from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm

from datetime import datetime


class TweetForm(forms.Form):
    tweet = forms.CharField(max_length = 140)
    target_language = forms.CharField(max_length=100)

