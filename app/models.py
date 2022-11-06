from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomUser

# Create your models here.

class Formfillup(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    step = models.PositiveSmallIntegerField(default=1, blank=True, null=True)
    dept_signature = models.ImageField(null=True, blank=True, upload_to='uploads/%Y-%m-%d')
    provost_signature = models.ImageField(null=True, blank=True, upload_to='uploads/%Y-%m-%d')
    register_signature = models.ImageField(null=True, blank=True, upload_to='uploads/%Y-%m-%d')
    payable_amount = models.IntegerField(blank=True, null=True)

    name = models.CharField(max_length=200, verbose_name='Name',)
    student_id = models.CharField(max_length=200, verbose_name='Student ID',)
    session = models.CharField(max_length=50, verbose_name='session',)
    # TODO: ekhan theke aro add kor field ja ja lagbe..
