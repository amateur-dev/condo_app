from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address', max_length=255, unique=True)
    f_name = models.CharField(max_length=64, blank=False, null=True)
    l_name = models.CharField(max_length=64, blank=False, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    condo_name = models.CharField(max_length=64, blank=False, null=True)
    unit_floor = models.PositiveSmallIntegerField(blank=False, null=True)
    unit_unit = models.PositiveSmallIntegerField(blank=False, null=True)
    has_access_to_facility = models.BooleanField(default=False, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True


class Condo(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    superuser = models.EmailField(max_length=64, unique=True, null=True)

    def __str__(self):
        return f"{self.id}: {self.name} located at {self.address}"


class Facility(models.Model):
    name = models.CharField(max_length=64)
    open_time = models.TimeField(null=True)
    close_time = models.TimeField(null=True)
    condo = models.ForeignKey(
        Condo, on_delete=models.CASCADE, related_name="condo")

    def __str__(self):
        return f"{self.origin} to {self.destination} in {self.duration} mins"
