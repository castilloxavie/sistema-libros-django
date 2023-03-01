from django import forms
from .models import Libros

class Libroform(forms.ModelForm):
    class Meta:
        model = Libros
        fields = '__all__'