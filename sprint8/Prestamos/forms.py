from django import forms

class PrestamoForm(forms.Form):
    tipo_prestamo = forms.ChoiceField(label="Tipo préstamo", choices=[('', 'Seleccione una opción'), ('HIPOTECARIO','Hipotecario'),('PRENDARIO','Prendario'),('PERSONAL','Personal')], required=True)
    fecha = forms.DateField(label="Fecha", required=True)
    monto = forms.DecimalField(label="Monto", required=True)