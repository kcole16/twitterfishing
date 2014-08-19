from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import RegexValidator

from core.models import Account

class TwitterHandle(models.Model):
	handle = models.CharField(max_length=1024, unique=True)


class Tweet(models.Model):
	user = models.ForeignKey(TwitterHandle)
	uid = models.CharField(max_length=160)
	raw_tweet = models.CharField(max_length=140)
	translated_tweet = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True)









