from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db.models.signals import post_save

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address', max_length=255, unique=True)
    f_name = models.CharField(max_length=64, blank=False, null=True)
    l_name = models.CharField(max_length=64, blank=False, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    condo_name = models.CharField(
        max_length=64, blank=True, null=True, default="Fortune Jade")
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

    # def save[dipesh to work on this]


class Condo(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    condo_admin = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


def create_condo(sender, instance, **kwargs):
    if kwargs['created']:
        condo_name_var = Condo.objects.create(name=instance.condo_name)
        # condo_name_var is for me to make further edits if I need to.


post_save.connect(create_condo, sender=CustomUser)


class Facility(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    first_booking_time = models.TimeField(null=True)
    last_booking_time_time = models.TimeField(null=True)
    condo = models.ForeignKey(
        Condo, on_delete=models.CASCADE, related_name="condo")

    def __str__(self):
        return f"{self.name}"
