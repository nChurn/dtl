from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser, AbstractUser, BaseUserManager,
    PermissionsMixin, Group as DjangoGroup)


class UserManager(BaseUserManager):
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD + '__iexact': username})


class User(PermissionsMixin, AbstractBaseUser):
    objects = UserManager()
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # attach methods from base user
    check_password = AbstractUser.check_password
    get_short_name = AbstractUser.get_short_name
    get_full_name = AbstractUser.get_full_name

    USERNAME_FIELD = 'email'


class Group(DjangoGroup):
    class Meta:
        proxy = True
