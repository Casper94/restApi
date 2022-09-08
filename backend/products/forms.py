from django import forms
from rest_framework import serializers
from .models import Product

class ProdutcForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
        ]