from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from myauth.models import User
from django.utils import timezone
from deptadmin.models import DepartmentPerson

GENDER_CHOICE = (
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other'),
)
COMPLAINT_CHOICE = (
    ('Normal','Normal'),
    ('Urgent','Urgent'),
    ('Lost','Lost'),
)
DEPARTMENT_CHOICE = (
    ('ADMIN', 'ADMIN'),
    ('Chief Warden','Chief Warden'),
    ('CSE','CSE'),
    ('HOSTEL OFFICE','HOSTEL OFFICE'),
)
STATUS_CHOICE = (
    ('COMPLAINT REGISTERED' , 'COMPLAINT REGISTERED'),
    ('UNDER DEPARTMENT VIEW' , 'UNDER DEPARTMENT VIEW'),
    ('PERSON ASSINGED TO SOLVE COMPLAINT' , 'PERSON ASSINGED TO SOLVE COMPLAINT'),
    ('NEED SOME REMARK' , 'NEED SOME REMARK'),
    ('SOLVED','SOLVED'),
    ('REJECTED','REJECTED'),
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

class complaintPost(models.Model):
    complaintId = models.AutoField(primary_key=True)
    complainthead = models.CharField(max_length=100 , blank=True)
    complaintType = models.CharField(max_length=20 , choices = COMPLAINT_CHOICE , default='Normal')
    complaintDes = models.TextField(blank=True)
    departmentType = models.ForeignKey(DepartmentPerson , on_delete=models.CASCADE)
    departmentChoice = models.CharField(max_length=30, choices=DEPARTMENT_CHOICE , default='ADMIN')
    s_reg = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=50 , choices=STATUS_CHOICE , default = 'COMPLAINT REGISTERED')
    sRemark = models.TextField(blank=True)
    assigneeRemark = models.TextField(blank=True)
    published_date = models.DateTimeField(blank=True, null=True)
    document = models.FileField(upload_to='doc_upload/')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.complainthead
