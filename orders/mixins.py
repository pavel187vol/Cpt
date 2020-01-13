from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, View, \
                                    DeleteView, UpdateView
from django.views.generic.edit import FormMixin
from .models import Order, ResponseOrder
from .forms import ResponseForm
from profiles.models import Customer, Executer
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy


class DetailObjectMixin(DetailView):
    model = None
    template_name = None

class RequiredCreateObjectMixin(object):
    """
    Разрешение к методу POST.
    """
    def post(self, request, *args, **kwargs):
        if request.user.id in self.users:
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        else:
            return redirect(reverse('login'))


class ExecuterObjectCreateMixin(RequiredCreateObjectMixin):
    """
    Только исполнитель может создать объект
    """
    def __init__(self):
        self.users = Executer.objects.values_list('user_id', flat=True)

class CustomerObjectCreateMixin(RequiredCreateObjectMixin):
    """
    Только заказчик может создать объект
    """
    def __init__(self):
        self.users = Customer.objects.values_list('user_id', flat=True)


class CreatorCustomerRequiredMixin(object):
    """
    Только для заказчика.
    """
    def get_queryset(self):
        queryset = super(CreatorCustomerRequiredMixin, self).get_queryset()
        return queryset.filter(customer=self.request.user.customer.get())



# class OrderDetailView(CustomerRequiredMixin, ResponseCreateMixin, DetailObjectMixin):
#     model = Order
#     context_object_name = 'order'
#     template_name = 'orders/manage/order/order_detail.html'
#     form_class = ResponseForm
#
#     def get_context_data(self, **kwargs):
#         context = super(OrderDetailView, self).get_context_data(**kwargs)
#         context['responses'] = ResponseOrder.objects.filter(order=self.object)
#         context['form'] = self.get_form()
#         context['executer_users'] = Executer.objects.values_list('user', flat=True)
#         context['creator'] = self.object.customer.user
#         return context

    # def post(self, request, *args, **kwargs):
    #     order = self.get_object()
    #     if request.POST.get('parent', None)\
    #     and order.customer.user == request.user:
    #         executer_id = request.POST.get('parent')
    #         executer = Executer.objects.get(id=executer_id)
    #         order = self.get_object()
    #         order.approv(executer)
    #         return redirect(reverse('order:order_list'))
    #     else:
    #         if request.user.executer.all():
    #             self.object = self.get_object()
    #             form = self.get_form()
    #             if form.is_valid():
    #                 return self.form_valid(form)
    #             else:
    #                 return self.form_invalid(form)
    #         else:
    #             return redirect(reverse('profile:register_executer'))
    #         return HttpResponse('у вас нет доступа')
