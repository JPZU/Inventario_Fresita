from django.db import models

# Create your models here.
class Products_principal(models.Model):
    product_id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=20, null=False)
    price = models.IntegerField(null=False)

    def __init__(self, product_id=None, name=None, price=None, *args, **kwargs):
        super(Products_principal, self).__init__(*args, **kwargs)
        self.product_id = product_id
        self.name = name
        self.price = price
    
class Sales_principal(models.Model):
    sale_id = models.AutoField(primary_key=True)
    date = models.DateField(null=False)
    product_id = models.ForeignKey('Products_principal', on_delete=models.CASCADE, null=False)
    quantity = models.SmallIntegerField(null=False)

    def __init__(self, *args, **kwargs):
        super(Sales_principal, self).__init__(*args, **kwargs)

    @classmethod
    def create(cls, date, product_id, quantity):
        sale = cls(date=date, product_id=product_id, quantity=quantity)
        return sale

    def __str__(self):
        return f"Sale ID: {self.sale_id}, Date: {self.date}, Product ID: {self.product_id}, Quantity: {self.quantity}"
    
class Inventories_principal(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey('Products_principal', on_delete=models.CASCADE, null=False)
    inventory_quantity = models.IntegerField(null=False)
    date_entry = models.DateField(null=False)
    
