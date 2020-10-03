from django.contrib import admin

from .models import *


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'date_created']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'description', 'date_created']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'product', 'date_created', 'status']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
