from django import forms
from django.contrib.auth.forms import UserCreationForm 
from Clientes.models import Sucursal, TipoCliente

class RegistrationForm(UserCreationForm):
    name = forms.CharField(label="Nombre", max_length=50, required=True)
    surname = forms.CharField(label="Apellido", max_length=50, required=True)
    mail = forms.EmailField(label="Mail", max_length=100, required=True)
    dni = forms.IntegerField(label="DNI", required=True, min_value=0)
    dob = forms.DateField(label="Fecha de Nacimiento", required=True)
    branch = forms.ModelChoiceField(queryset=Sucursal.objects.all().order_by('branch_name'),  label="Sucursal", required=True)
    client_type = forms.ModelChoiceField(queryset=TipoCliente.objects.all(), label="Tipo de Cliente", required=True)

    widgets = {
            'name': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }
