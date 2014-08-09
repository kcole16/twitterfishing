from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm

from datetime import datetime

from core.models import Account, AccountManager


class AccountForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		super(AccountForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Account
		fields = ('yo_name', 'password')