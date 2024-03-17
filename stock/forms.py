from django import forms
from .models import Products

   
class ProductsForm(forms.Form):
    name = forms.CharField(label="Product name", max_length=50)
    price = forms.IntegerField(label="price", min_value=0)