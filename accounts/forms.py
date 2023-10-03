from django import forms
from django import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'


