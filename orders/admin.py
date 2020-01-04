from django.contrib import admin
from .models import Order, ResponseOrder

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['title', 'customer', 'executer', 'condition']
    list_filter = ['condition']
    search_fields = ['title','customer', 'executer']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(ResponseOrder)
class ResponseOrderAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'executer']
