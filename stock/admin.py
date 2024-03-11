from django.contrib import admin

from .models import Products,Sales, Inventories, Inventories_sales
# Register your models here.

admin.site.register(Products)
admin.site.register(Sales)
admin.site.register(Inventories)
admin.site.register(Inventories_sales)
