from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, View, \
                                    DeleteView
from django.views.generic.edit import FormMixin
from .models import Order, ResponseOrder
from .forms import ResponseForm
from profiles.models import Customer, Executer
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy



class OrderDetailView(FormMixin, DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'orders/manage/order/order_detail.html'
    form_class = ResponseForm

    def get_success_url(self):
       return reverse('order:order_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        context['responses'] = ResponseOrder.objects.filter(order=self.object)
        context['form'] = self.get_form()
        context['executer_users'] = Executer.objects.values_list('user', flat=True)
        context['creator'] = Customer.objects.get(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.executer = Executer.objects.get(user=self.request.user)
        form.instance.order = self.object
        form.save()
        return super(OrderDetailView, self).form_valid(form)

class OrderListView(ListView):
    model = Order
    context_object_name = 'orders'
    queryset = Order.objects.filter(condition=False)
    template_name = 'orders/manage/order/order_list.html'

class OrderCreateView(CreateView):
    model = Order
    fields = ['title', 'text', 'image', 'price']
    success_url = '/'
    template_name = 'orders/manage/order/order_create.html'

    def form_valid(self, form):
        # customer =
        form.instance.customer = Customer.objects.get(user=self.request.user)
        return super().form_valid(form)

class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('order:order_list')
    template_name = 'orders/manage/order/order_delete.html'
