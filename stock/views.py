from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum
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

def salesDate(request, date):
    sales = Sales.objects.filter(date=date)
    
    # Calcular el total vendido en el día
    total_sold_in_day = sales.aggregate(total_sold=Sum('quantity'))['total_sold'] or 0
    
    total_sales_by_date = {}

    for sale in sales:
        date = sale.date
        if date in total_sales_by_date:
            total_sales_by_date[date] += sale.quantity * sale.product_id.price
        else:
            total_sales_by_date[date] = sale.quantity * sale.product_id.price

    context = {
        'date': date,
        'sales': sales,
        'total_sold_in_day': total_sold_in_day,
        'total_sales_by_date': total_sales_by_date,
    }
    return render(request, "stock/salesDate.html", context)