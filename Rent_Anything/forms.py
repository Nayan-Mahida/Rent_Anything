from django import forms
from .models import items


class itemsForm(forms.ModelForm):
    class Meta:
        model = items
        fields = '__all__'