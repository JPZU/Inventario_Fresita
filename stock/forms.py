from django import forms
from .models import Sales, Products

class ProductNameChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class SalesForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    product_id = ProductNameChoiceField(queryset=Products.objects.all())

    class Meta:
        model = Sales
        fields = ['date', 'product_id', 'quantity']
