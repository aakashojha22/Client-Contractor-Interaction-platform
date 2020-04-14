from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect


occupation_CHOICES = (
    ('contractor','Contractor'),
    ('interior designer','Interior Designer'),
    ('map designer','Map Designer'),
)


# Just checking the update Create your models here.
class ContractorLogin(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20,unique=False,null=True)
    mobile_no = models.BigIntegerField(blank=True, null=True)
    address = models.CharField(max_length=150,unique=False,null=True)
    occupation  = models.CharField(max_length=50,choices=sorted(occupation_CHOICES),default='null')
    experience = models.IntegerField(blank=True, null=True)
    about_self = models.CharField(max_length=150,null=True,blank=True)
    profile_pic=models.ImageField(upload_to='profile_pic',blank=True)
    sample_work_1=models.ImageField(upload_to='sample_work_1',blank=True)
    sample_work_2=models.ImageField(upload_to='sample_work_2',blank=True)
    sample_work_3=models.ImageField(upload_to='sample_work_3',blank=True)
    sample_work_4=models.ImageField(upload_to='sample_work_4',blank=True)
    sample_work_5=models.ImageField(upload_to='sample_work_5',blank=True)
    sample_work_6=models.ImageField(upload_to='sample_work_6',blank=True)


    def get_absolute_url(self):
        return redirect("contractor:thankyou")


    def __str__(self):
        return  self.user.username



