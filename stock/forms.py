from django import forms
from .models import *

class SalesForm(forms.ModelForm):
    product_id = forms.ModelChoiceField(queryset=Products.objects.all(), to_field_name="name")
    class Meta:
        model = Sales
        fields = ['date', 'product_id', 'quantity']
    