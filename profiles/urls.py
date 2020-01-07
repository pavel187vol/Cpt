from django.urls import path
from . import views
app_name = 'profile'

urlpatterns = [
    path('register_customer/', views.CustomerProfileCreateView.as_view(), name='register_customer'),
    path('register_executer/', views.ExecuterProfileCreateView.as_view(), name='register_executer'),
    path('executer_list/', views.ExecuterListView.as_view(), name='executer_list'),
    path('customer_list/', views.CustomerListView.as_view(), name='customer_list'),
    path('executer/<slug>/', views.ExecuterDetailView.as_view(), name='executer_detail'),
    path('customer/<slug>/', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('my_profile/executer/<slug>/', views.MyProfileExecuter.as_view(), name='my_profile_executer'),
    path('my_profile/customer/<slug>/', views.MyProfileCustomer.as_view(), name='my_profile_customer'),
]
