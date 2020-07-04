from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,DetailView,
                                  CreateView,DeleteView,UpdateView)
from .forms import ClientLoginForm,ProjectDetailForm
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import  ClientLogin,Bid
from django.contrib.auth import authenticate, login
from Contractor.models import ContractorLogin
from django.contrib.auth.models import User

class IndexView(TemplateView):
    template_name = 'client/index.html'

class ClientIndexView(TemplateView):
    template_name = 'client/client_index.html'

class Profile(TemplateView):
    template_name = 'client/profile.html'

def signup(request):

    if request.method =='POST':
        user_form = ClientLoginForm(data=request.POST)
        profile_form = ProjectDetailForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user=user

            profile.save()
            return redirect('client:thankyou')
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=ClientLoginForm()
        profile_form = ProjectDetailForm()
    return render(request,'client/signup.html',{
            'user_form':user_form,
            'profile_form':profile_form,
        })



class ThankyouView(TemplateView):
    template_name = 'client/thankyou.html'




def user_login(request):

    if request.method== 'POST':
        username=request.POST.get('username')
        password = request.POST.get('password')

        user= authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('client:client_index'))

            else:
                return HttpResponse("account not active")

        else:
            info='login failed'
            return render(request,'client/login.html',{'message':info})

    else:
        return render(request,'client/login.html',{})



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('client:index'))


class List(ListView,LoginRequiredMixin):
    model = ContractorLogin
    template_name = 'client/contractor_list.html'

class ContractorProfileView(DetailView,LoginRequiredMixin):
    model = ContractorLogin
    template_name = 'client/contractor_profile.html'

class UserContractorProfileView(DetailView,LoginRequiredMixin):
    model = User
    template_name = 'client/user_contractor_profile.html'

class BidList(ListView,LoginRequiredMixin,):
    model = Bid
    template_name = 'client/bid_list.html'
    def get_queryset(self):
        return Bid.objects.filter().order_by('-bid_created_at')


