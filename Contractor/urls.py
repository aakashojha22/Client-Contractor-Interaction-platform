
from django.urls import path
from django.contrib.auth import views as v
from  . import views

app_name='contractor'

urlpatterns = [
            path('',views.IndexView.as_view(),name='index'),
            path('signup',views.signup,name='signup'),
            path('thankyou', views.ThankyouView.as_view(), name='thankyou'),
            path('login', v.LoginView.as_view(template_name='contractor/login.html'), name='login'),
            path('logout', views.user_logout, name='logout'),
            path('profile',views.ContractorProfile.as_view(),name='contractor_profile'),
            path('client_list',views.ClientListView.as_view(),name='client_list'),
            path('client_profile/<int:pk>/', views.ClientProfileView.as_view(), name='client_profile_view'),
            path('place_bid/<int:client_pk>/<int:contractor_pk>', views.create_bid, name='place_bid'),

]



