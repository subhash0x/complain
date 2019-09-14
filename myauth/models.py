from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICE = (
        (1,'student'),
        (2,'administrator'),
        (3,'assignee'),
    )
    user_type = models.PositiveSmallIntegerField(choices = USER_TYPE_CHOICE, default=1)
