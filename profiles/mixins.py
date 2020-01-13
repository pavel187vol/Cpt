from django.shortcuts import render
from .models import Customer, Executer
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView
from .forms import CustomerProfileInfoForm, ExecuterProfileInfoForm, UserForm
from django.views.generic.base import TemplateResponseMixin, View
from orders.models import Order

class UserProfileCreateMixin(TemplateResponseMixin, View):
    """
    Регистрация профиля(заказчик/исполнитель).
    """
    form_class = None

    def get(self, request, *args, **kwargs):
        context = {'user_form': UserForm(),'profile_form': self.form_class}
        return render(request, 'profiles/register.html', context)

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
        return render(request, 'profiles/register.html',
                                {'user_form': user_form,
                                'profile_form': profile_form,
                                'registered':registered})

class UserListMixin(object):
    """
    Все исполнители/заказчики.
    """
    model = None
    paginate_by = 2

    def get_queryset(self):
        return self.model.objects.order_by('id')

class MyProfileModel(View):
    """
    Личный кабинет.
    """
    model = None

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
