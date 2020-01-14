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
from .mixins import *

class OrderDetailView(ExecuterObjectCreateMixin, FormMixin, DetailObjectMixin):
    model = Order
    context_object_name = 'order'
    template_name = 'orders/order_detail.html'
    form_class = ResponseForm

    def get_success_url(self):
       return reverse('order:order_detail', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        context['responses'] = ResponseOrder.objects.filter(order=self.object)
        context['form'] = self.get_form()
        return context

    def form_valid(self, form):
        self.object = self.get_object()
        form.instance.executer = Executer.objects.get(user=self.request.user)
        form.instance.order = self.object
        form.save()
        return super(OrderDetailView, self).form_valid(form)

class OrderListView(ListView):
    model = Order
    context_object_name = 'orders'
    queryset = Order.objects.filter(condition=False)
    template_name = 'orders/order_list.html'
    paginate_by = 5


class OrderCreateView(CustomerObjectCreateMixin, CreateView):
    model = Order
    fields = ['title', 'text', 'image', 'price']
    template_name = 'orders/order_create.html'

    def get_success_url(self):
        return reverse('order:order_detail',kwargs={'slug':self.object.slug})

    def form_valid(self, form):
        form.instance.customer = Customer.objects.get(user=self.request.user)
        return super().form_valid(form)

class OrderDeleteView(CreatorCustomerRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('order:order_list')
    template_name = 'orders/order_delete.html'
