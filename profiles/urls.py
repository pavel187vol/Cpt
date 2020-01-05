from django.urls import path
from . import views
app_name = 'profile'

urlpatterns = [
    path('profile/register_customer/', views.CustomerProfileCreateView.as_view(), name='register_customer'),
    path('profile/register_executer/', views.ExecuterProfileCreateView.as_view(), name='register_executer'),
    path('profile/executer_list', views.ExecuterListView.as_view(), name='executer_list'),
    path('profile/customer_list', views.CustomerListView.as_view(), name='customer_list'),
    path('profile/executer/<slug>/', views.ExecuterDetailView.as_view(), name='executer_detail'),
    path('profile/customer/<slug>/', views.CustomerDetailView.as_view(), name='customer_detail'),
]
