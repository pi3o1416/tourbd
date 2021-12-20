from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.validators import UnicodeUsernameValidator

# Create your models here.


class CustomUser(AbstractUser):

    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
        blank=False
    )

    email = models.EmailField(
        _('email address'),
        unique=True,
        blank=False,
    )
    date_of_birth = models.DateField(
        _("Date of Birth"),
        blank=True,
        default=timezone.now,
    )
    interest = ArrayField(
        models.CharField(max_length=30, blank=True),
        size=4,
        default=list,
    )
    class Meta:
        permissions = [
            ('can_create_post', 'Can create post'),
            ('can_delete_post', 'Can delete post'),
            ('can_update_post', 'Can update post'),
            ('can_view_post', 'Can view post'),
            ('can_create_comment', 'Can create comment'),
        ]





