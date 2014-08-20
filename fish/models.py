from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Tweet(models.Model):
	user = models.ForeignKey(User)
	uid = models.CharField(max_length=160)
	raw_tweet = models.CharField(max_length=140)
	translated_tweet = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True)









