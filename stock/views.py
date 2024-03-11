from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    products = Products.objects.all()
    sales = Sales.objects.all()

    total_sales_by_date = {}

    for sale in sales:
        date = sale.date
        if date in total_sales_by_date:
            total_sales_by_date[date] += sale.quantity * sale.product_id.price
        else:
            total_sales_by_date[date] = sale.quantity * sale.product_id.price

    return render(request, "stock/index.html", {'products': products, 'sales': sales, 'total_sales_by_date': total_sales_by_date})
