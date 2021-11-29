from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(
        _("Date of Birth"),
        blank=True,
        default=timezone.now,
    )
    interest = ArrayField(
        ArrayField(
            models.CharField(max_length=30, blank=True),
        ),
        size=4,
        default=list,
    )
