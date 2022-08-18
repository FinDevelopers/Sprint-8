from pyexpat import model
from django import forms
from .models import Tarjeta

class TarjetaForm(forms.ModelForm):
    class Meta:
        model = Tarjeta
        fields = ['brand','card_type']