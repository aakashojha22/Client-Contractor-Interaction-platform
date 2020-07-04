
from django.urls import path
from django.contrib.auth import views as v
from  client import views

app_name='client'

#app_name='client'

urlpatterns = [
            path('',views.IndexView.as_view(),name='index'),
            path('signup',views.signup,name='signup'),
            path('thankyou', views.ThankyouView.as_view(), name='thankyou'),
            path('login', views.user_login, name='user_login'),
            path('logout', views.user_logout, name='logout'),
            path('client_index',views.ClientIndexView.as_view(),name='client_index'),
            path('profile',views.Profile.as_view(),name='client_profile'),
            path('list',views.List.as_view(),name='list'),
            path('bid_list',views.BidList.as_view(),name='bid_list'),
            path('contractor_profile/<int:pk>/', views.ContractorProfileView.as_view(), name='contractor_profile_view'),
            path('User_contractor_profile/<int:pk>/', views.UserContractorProfileView.as_view(), name='user_contractor_profile_view'),
]



