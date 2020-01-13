from django.shortcuts import render
from .models import Customer, Executer
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView
from .forms import CustomerProfileInfoForm, ExecuterProfileInfoForm, UserForm
from django.views.generic.base import TemplateResponseMixin, View
from orders.models import Order
from .mixins import *

class CustomerProfileCreateView(UserProfileCreateMixin,
                                CreateView):
    form_class = CustomerProfileInfoForm

class ExecuterProfileCreateView(UserProfileCreateMixin,
                                CreateView):
    form_class = ExecuterProfileInfoForm

class CustomerListView(UserListMixin, ListView):
    model = Customer

class ExecuterListView(UserListMixin, ListView):
    model = Executer

class ExecuterDetailView(DetailView):
    model = Executer

    def get_context_data(self, **kwargs):
        context = super(ExecuterDetailView, self).get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(executer=self.object,
                                                condition=True)
        context['success_order'] = Order.objects.filter(executer=self.object,
                                                condition=True,
                                                condition_success=True)
        return context

class CustomerDetailView(DetailView):
    model = Customer

    def get_context_data(self, **kwargs):
        context = super(CustomerDetailView, self).get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(customer=self.object,
                                                condition=False)
        return context

class MyProfileCustomer(MyProfileModel, DetailView):
    model = Customer
    template_name = 'profiles/manage/profile/my_profile_customer.html'

class MyProfileExecuter(MyProfileModel, DetailView):
    model = Executer
    template_name = 'profiles/manage/profile/my_profile_executer.html'
