from django.contrib import admin

from .models import Products_principal,Sales_principal, Inventories_principal
# Register your models here.

admin.site.register(Products_principal)
admin.site.register(Sales_principal)
admin.site.register(Inventories_principal)


