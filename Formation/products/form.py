from django import forms
from .models import products

class ProductForm(forms.ModelForm):
    class Meta:
        model = products
        fields = ('name', 'description', 'price', 'image', 'slug')