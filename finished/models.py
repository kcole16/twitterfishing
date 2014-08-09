from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import RegexValidator

from core.models import Account


class Item(models.Model):
	@classmethod
	def create(cls, user, content, date_posted):
		item = cls(user=user, content=content, date_created=date_created, date_started=date_started,
			date_ended=date_ended)
		return post

	user = models.ForeignKey(Account)
	content = models.CharField(max_length=500)
	date_created = models.DateTimeField(auto_now_add=True)
	date_started = models.DateTimeField(null=True)
	date_ended = models.DateTimeField(null=True)
	time_to_complete = models.TimeField(null=True)




