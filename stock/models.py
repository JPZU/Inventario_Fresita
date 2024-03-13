from django.db import models

# Create your models here.
class Products(models.Model):
    product_id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=20, null=False)
    price = models.IntegerField(null=False)
    
class Sales(models.Model):
    sale_id = models.AutoField(primary_key=True)
    date = models.DateField(null=False)
    product_id = models.ForeignKey('Products', on_delete=models.CASCADE, null=False)
    quantity = models.SmallIntegerField(null=False)
    
class Inventories(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey('Products', on_delete=models.CASCADE, null=False)
    inventory_quantity = models.IntegerField(null=False)
    date_entry = models.DateField(null=False)
    
class Inventories_sales(models.Model):
    inventory_sales_id = models.AutoField(primary_key=True)
    inventory_id = models.ForeignKey('Inventories', on_delete=models.CASCADE)
    sale_id = models.ForeignKey('Sales', on_delete=models.CASCADE)

# models.py



