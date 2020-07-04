from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,DetailView,
                                  CreateView,DeleteView,UpdateView)
from .forms import ContractorLoginForm,ContractorDetailForm,CreateBidForm
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import  ContractorLogin
from client.models import ClientLogin
from django.contrib.auth.models import User



class IndexView(TemplateView):
    template_name = 'contractor/index.html'


class ContractorProfile(TemplateView):
    template_name = 'contractor/profile.html'





def signup(request):

    if request.method =='POST':
        user_form = ContractorLoginForm(data=request.POST)
        profile_form = ContractorDetailForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user=user
            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
			if 'sample_work_1' in request.FILES:							
                profile.sample_work_1=request.FILES['sample_work_1']
            if 'sample_work_2' in request.FILES:
                profile.sample_work_2=request.FILES['sample_work_2']
            if 'sample_work_3' in request.FILES:
                profile.sample_work_3=request.FILES['sample_work_3']
            if 'sample_work_4' in request.FILES:
                profile.sample_work_4=request.FILES['sample_work_4']
            if 'sample_work_5' in request.FILES:
                profile.sample_work_5=request.FILES['sample_work_5']
            if 'sample_work_6' in request.FILES:
                profile.sample_work_6=request.FILES['sample_work_6']

            profile.save()
            return redirect('contractor:thankyou')

        else:
            print(user_form.errors,profile_form.errors)


    else:
        user_form=ContractorLoginForm()
        profile_form=ContractorDetailForm()

    return render(request,'contractor/signup.html',{
            'user_form':user_form,
            'profile_form':profile_form ,

        })

class ThankyouView(TemplateView):
    template_name = 'contractor/thankyou.html'



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('contractor:index'))

class ClientListView(ListView,LoginRequiredMixin):
    model = ClientLogin
    template_name = 'contractor/client_list.html'
    #def get_queryset(self):project_created_at
       #return ClientRequest.objects.filter(appointment_date__gte=timezone.now(),request_status='service_pending').order_by('appointment_date')
    def get_queryset(self):
        return ClientLogin.objects.filter().order_by('-project_created_at')


class ClientProfileView(DetailView,LoginRequiredMixin):
    model = ClientLogin
    template_name = 'contractor/client_profile.html'

def create_bid(request,client_pk,contractor_pk):
    form = CreateBidForm()
    if request.method == "POST":
        form = CreateBidForm(request.POST)
        if form.is_valid():
            request_detail = form.save(commit=False)
            request_detail.from_contractor = request.user
            client_id = User.objects.get(pk=client_pk)
            request_detail.to_client = client_id
            request_detail.from_contractor_pk = contractor_pk
            request_detail.save()
            return redirect('contractor:client_list')
    return render(request, 'contractor/place_bid_form.html', {'form': form})
