from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect


material_CHOICES = (
    ('without_material','Without Material'),
    ('with_material','With Material'),

)

class ClientLogin(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20,unique=False,null=True)
    budget = models.PositiveIntegerField(blank=True,null=True)
    mobile_no = models.BigIntegerField(unique=True)
    plot_size = models.PositiveIntegerField(blank=True,null=True)
    address = models.CharField(max_length=150,unique=False,null=True)
    bedrooms = models.PositiveSmallIntegerField(blank=True,null=True)
    bathrooms = models.PositiveSmallIntegerField(blank=True,null=True)
    floors = models.PositiveSmallIntegerField(blank=True,null=True)
    description = models.TextField(blank=True,unique=False,null=True)
    project_created_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return redirect("index")

    def __str__(self):
        return  self.user.username

class Bid(models.Model):
    from_contractor = models.ForeignKey(User, related_name='from_contractor', on_delete=models.CASCADE)
    from_contractor_pk = models.PositiveIntegerField(null=True)
    to_client = models.ForeignKey(User, related_name='to_client', on_delete=models.CASCADE,null=True)
    bid_created_at = models.DateTimeField(auto_now=True)
    amount = models.PositiveIntegerField(blank=True,null=True)
    material = models.CharField(max_length=50, choices=sorted(material_CHOICES), default='without_material')

    def __str__(self):
        return str(self.from_contractor )

