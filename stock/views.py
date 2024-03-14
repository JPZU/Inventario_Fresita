from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum
from .models import Sales,Products, Inventories,Inventories_sales
import pdb


def index(request):
    products = Products.objects.all()
    sales = Sales.objects.all()
    
    # Calcula la cantidad total vendida por producto y el valor total por producto
    sold_quantity_per_product = {}
    total_value_per_product = {}

    for product in products:
        total_sold = sales.filter(product_id=product).aggregate(total_sold=Sum('quantity'))['total_sold'] or 0
        total_inventory = Inventories.objects.filter(product_id=product).aggregate(total_inventory=Sum('inventory_quantity'))['total_inventory'] or 0
        sold_quantity_per_product[product] = max(total_inventory - total_sold, 0)
        total_value_per_product[product] = product.price * sold_quantity_per_product[product]

    total_value_per_product = sum(total_value_per_product.values())
    
    # pdb.set_trace() 
    context = {
        'products': products, 
        'sales': sales,
        'sold_quantity_per_product': sold_quantity_per_product,
        'total_value_per_product': total_value_per_product,  
    }      

    return render(request, "stock/index.html", context)


def enterSales(request):
    return render(request, "stock/enterSales.html")


def enterStock(request):
    return render(request, "stock/enterStock.html")


def salesHistory(request):
    searchTerm = request.GET.get('searchDate')
    
    sales = Sales.objects.filter(date=searchTerm)
    last_date = Sales.objects.latest('date')
    last_date = last_date.date
    
    # Calcular el total vendido en el día
    total_sold_in_day = sales.aggregate(total_sold=Sum('quantity'))['total_sold'] or 0
    
    total_sales_by_date = {}

    for sale in sales:
        date = sale.date
        if date in total_sales_by_date:
            total_sales_by_date[date] += sale.quantity * sale.product_id.price
        else:
            total_sales_by_date[date] = sale.quantity * sale.product_id.price

    # pdb.set_trace()
    context = {
        'last_date':last_date ,
        'sales': sales,
        'total_sold_in_day': total_sold_in_day,
        'total_sales_by_date': total_sales_by_date,
    }
    return render(request, "stock/salesHistory.html", context)

def stadistics(request):
    return render(request, "stock/stadis.html")