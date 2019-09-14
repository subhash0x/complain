from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from myauth.models import User

GENDER_CHOICE = (
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other'),
)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100 , blank=True)
    reg_no = models.CharField(primary_key = True , max_length=10)
    roll_no = models.IntegerField(blank=True,default = 0)
    course = models.CharField(max_length=50 , blank=True)
    year = models.IntegerField(blank=True,default=0)
    gender = models.CharField(max_length=20, choices = GENDER_CHOICE , default='Male')

    def publish(self):
        self.save()

    def __str__(self):
        return self.reg_no
