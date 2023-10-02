from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'  # You can specify the fields you want to include here if needed

