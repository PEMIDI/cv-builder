from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import ugettext as _


class CustomUser(AbstractUser):
    """
    CustomUser model extending the AbstractUser model provided by Django's authentication framework.

    Fields:
    - username: The username of the user (inherited from AbstractUser)
    - password: The password of the user (inherited from AbstractUser)
    - email: The email address of the user (inherited from AbstractUser)
    - first_name: The first name of the user (inherited from AbstractUser)
    - last_name: The last name of the user (inherited from AbstractUser)
    - phone_number: The phone number of the user (optional)
    """

    phone_number = models.CharField(verbose_name=_('phone number'), max_length=12, blank=True)
