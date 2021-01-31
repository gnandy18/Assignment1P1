from django import forms
from .models import Request, Item


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        # fields = ('username', 'bag', 'food_allergy', 'request_date', 'additional_request')
        fields = ('bag', 'food_allergy', 'request_date', 'additional_request')


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('item_name', 'item_quantity', 'item_description')
