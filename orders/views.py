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


class OrderDetailView(FormMixin, DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'orders/manage/order/order_detail.html'
    form_class = ResponseForm

    def get_success_url(self):
       return reverse('order:order_detail', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        context['responses'] = ResponseOrder.objects.filter(order=self.object)
        context['form'] = self.get_form()
        context['executer_users'] = Executer.objects.values_list('user', flat=True)
        context['creator'] = self.object.customer.user
        return context

    def post(self, request, *args, **kwargs):
        if request.POST.get('parent', None):
            executer_id = request.POST.get('parent')
            executer = Executer.objects.get(id=executer_id)
            order = self.get_object()
            order.approv(executer)
            return HttpResponse(executer)
        elif request.user.executer.all():
            return HttpResponseForbidden()
        else:
            return HttpResponse(executers.count())
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
    success_url = 'order:order_list'
    template_name = 'orders/manage/order/order_create.html'


    def get(self, request, *args, **kwargs):
        customers = Customer.objects.all()
        if request.user.customer.all():
            return super().post(request, *args, **kwargs)
        return redirect(self.success_url)

    def post(self, request, *args, **kwargs):
        customers = Customer.objects.values_list('user', flat=True)
        if request.user in customers:
            return HttpResponseForbidden()
        else:
            return HttpResponse('p')
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.customer = Customer.objects.get(user=self.request.user)
        return super().form_valid(form)

class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('order:order_list')
    template_name = 'orders/manage/order/order_delete.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.customer.user != self.request.user:
            return redirect(self.success_url)
        return super().post(request, *args, **kwargs)

class ResponseOrderDetailView(DetailView):
    model = ResponseOrder
    context_object_name = 'response'
    template_name = 'orders/manage/order/response_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.order.customer.user != self.request.user:
            return redirect('order:order_list')
        return super().post(request, *args, **kwargs)

    def post(self,request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_object()
        form.order.approv(form.executer)
        return HttpResponse(form.order)
