from django import forms
from django.contrib.auth.models import User
from .models import ClientLogin


class ClientLoginForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields=('username','email','password')


class ProjectDetailForm(forms.ModelForm):
    name = forms.CharField(label='Your name', max_length=20)
    budget = forms.IntegerField(label='Budget', )
    mobile_no = forms.IntegerField(label='Mobile(Without Country code)', )
    plot_size = forms.IntegerField(label='Plot Size (in square feet)', )
    address = forms.CharField(label='Full Address of Plot',max_length=150 )
    bedrooms = forms.IntegerField(label='No. of Bedrooms',)
    bathrooms = forms.IntegerField(label='No. of Bathrooms ', )
    floors = forms.IntegerField(label='No. of Floors', )

    class Meta():
        model = ClientLogin
        fields=('name','mobile_no','budget','plot_size','bedrooms','bathrooms','floors','address','description',)

    def clean(self):
        # data from the form is fetched using super function
        super(ProjectDetailForm, self).clean()

        # extract the username and text field from the data
        mobile_no = str(self.cleaned_data.get('mobile_no'))


        # conditions to be met for the username length
        if len(mobile_no) != 10:
            self._errors['mobile_no'] = self.error_class([
                'Minimum 10 characters required'])