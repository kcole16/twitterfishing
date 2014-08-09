from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import RegexValidator
class AccountManager(BaseUserManager):
    def create_user(self, yo_name, password=None):
        if not yo_name:
            raise ValueError('Users must have a Yo account')

        user = self.model(yo_name=yo_name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, yo_name, password):
        user = self.create_user(yo_name, password)
        user.yo_name = yo_name
        user.is_admin = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser, PermissionsMixin):
    yo_name = models.CharField(max_length=1024, unique=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'yo_name'
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.yo_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

