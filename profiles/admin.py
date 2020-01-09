from django.contrib import admin
from .models import Customer, Executer

@admin.register(Customer)
class CumstomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone',
                    'email','city']
    list_filter = ['first_name']
    search_fields = ['first_name', 'last_name',
                     'phone', 'email']

@admin.register(Executer)
class ExecuterAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone',
                    'email', 'city']
    list_filter = ['first_name']
    search_fields = ['first_name', 'last_name',
                     'phone', 'email']
