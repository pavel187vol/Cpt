from django.shortcuts import render
from .models import Customer, Executer
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView
from .forms import CustomerProfileInfoForm, ExecuterProfileInfoForm, UserForm
from django.views.generic.base import TemplateResponseMixin, View
from orders.models import Order

class UserProfileCreateMixin(TemplateResponseMixin, View):
    form_class = None

    def get(self, request, *args, **kwargs):
        context = {'user_form': UserForm(),'profile_form': self.form_class}
        return render(request, 'profiles/manage/profile/register.html', context)

    def post(self, request, *args, **kwargs):
        registered = False
        user_form = UserForm(data=request.POST)
        profile_form = self.form_class(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
        return render(request, 'profiles/manage/profile/register.html',
                                {'user_form': user_form,
                                'profile_form': profile_form,
                                'registered':registered})

class CustomerProfileCreateView(UserProfileCreateMixin,
                                CreateView):
    form_class = CustomerProfileInfoForm

class ExecuterProfileCreateView(UserProfileCreateMixin,
                                CreateView):
    form_class = ExecuterProfileInfoForm

class CustomerListView(ListView):
    models = Customer
    context_object_name = 'customers'
    template_name = 'profiles/manage/profile/customer_list.html'

    def get_queryset(self):
        """"""
        return Customer.objects.order_by('id')

class ExecuterListView(ListView):
    models = Executer
    context_object_name = 'executers'
    template_name = 'profiles/manage/profile/executer_list.html'

    def get_queryset(self):
        """"""
        return Executer.objects.order_by('id')

class ExecuterDetailView(DetailView):
    model = Executer
    context_object_name = 'executer'
    template_name = 'profiles/manage/profile/executer_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ExecuterDetailView, self).get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(executer=self.object,
                                                condition=True)
        return context

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'profiles/manage/profile/customer_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CustomerDetailView, self).get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(customer=self.object,
                                                condition=False)
        return context

class MyProfileModel(View):
    model = None

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

class MyProfileCustomer(MyProfileModel, DetailView):
    model = Customer
    template_name = 'profiles/manage/profile/my_profile_customer.html'

class MyProfileExecuter(MyProfileModel, DetailView):
    model = Executer
    template_name = 'profiles/manage/profile/my_profile_executer.html'
