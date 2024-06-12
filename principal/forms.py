from django import forms
from .models import Sales_principal, Products_principal

class ProductNameChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class SalesForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    product_id = ProductNameChoiceField(queryset=Products_principal.objects.all())

    class Meta:
        model = Sales_principal
        fields = ['date', 'product_id', 'quantity']
