from django.urls import path
from . import views

app_name='order'

urlpatterns = [
    path('', views.OrderListView.as_view(), name='order_list'),
    path('order/<slug>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('create/', views.OrderCreateView.as_view(), name='order_create'),
    path('delete/<slug>/', views.OrderDeleteView.as_view(), name='order_delete'),
    path('response/<pk>', views.ResponseOrderDetailView.as_view(), name='response_detail')
    # path('update/<slug>/', views.OrderExecuterUpdateView.as_view(), name='order_update'),
]
