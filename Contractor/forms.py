from django import forms
from django.contrib.auth.models import User
from .models import ContractorLogin
from client.models import  Bid

class ContractorLoginForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields=('username','email','password')

class ContractorDetailForm(forms.ModelForm):
    class Meta():
        model = ContractorLogin
        fields=('name','mobile_no','address','occupation','experience','about_self','profile_pic','sample_work_1',
                'sample_work_2','sample_work_3','sample_work_4','sample_work_5','sample_work_6')

class CreateBidForm(forms.ModelForm):
    class Meta():
        model = Bid
        fields=("amount","material")


