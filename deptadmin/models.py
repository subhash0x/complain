from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from myauth.models import User

GENDER_CHOICE = (
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other'),
)

class DepartmentPerson(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100 , blank=True)
    deptId = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=20, choices = GENDER_CHOICE , default='Male')

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
