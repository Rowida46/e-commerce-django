
from django import forms
from categories.models import Categories


class CreateForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'
        