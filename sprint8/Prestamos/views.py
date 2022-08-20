from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import PrestamoForm
from .models import Prestamo



# Create your views here.
@login_required(login_url='/login/')
def formulario(request):
    usuario_nombre = request.user.get_full_name()
    prestamo_form = PrestamoForm
    if request.method == 'POST':
        prestamo_form = PrestamoForm(request.POST)
        if prestamo_form.is_valid():
            monto =  float(request.POST.get('monto')) * 100
            cuenta = request.user.cliente.cuentas.get(account_type = 3)
            tipo_cliente = request.user.cliente.client_type.clt_name
            if tipo_cliente == 'Classic' and monto > 10000000:
                error_message = "Su tipo de cuenta 'Classic' tiene un límite de $100.000,00 para préstamos."
                return render(request, 'Prestamos/formulario.html', {'usuario_nombre': usuario_nombre, 'prestamo_form': prestamo_form,'error_message':error_message})
            if tipo_cliente == 'Gold' and monto > 30000000:
                error_message = "Su tipo de cuenta 'Gold' tiene un límite de $300.000,00 para préstamos."
                return render(request, 'Prestamos/formulario.html', {'usuario_nombre': usuario_nombre, 'prestamo_form': prestamo_form,'error_message':error_message})
            if tipo_cliente == 'Black' and monto > 50000000:
                error_message = "Su tipo de cuenta 'Black' tiene un límite de $500.000,00 para préstamos."
                return render(request, 'Prestamos/formulario.html', {'usuario_nombre': usuario_nombre, 'prestamo_form': prestamo_form,'error_message':error_message})
            prestamo = Prestamo()
            prestamo.loan_type = request.POST.get('tipo_prestamo')
            prestamo.loan_date = request.POST.get('fecha')
            prestamo.loan_total = monto
            prestamo.customer = request.user.cliente

            cuenta.recibir_prestamo(monto)
            prestamo.save()
            return redirect(reverse('Prestamos')+'?status=success')
    return render(request, 'Prestamos/formulario.html', {'usuario_nombre': usuario_nombre, 'prestamo_form': prestamo_form})

@login_required(login_url='/login/')
def prestamos(request):
    usuario_nombre = request.user.get_full_name()
    prestamos = request.user.cliente.prestamos.all()
    success_message = ''
    if request.GET.get('status','') == 'success':
        success_message = 'Préstamo añadido con éxito'
    return render(request, 'Prestamos/prestamos.html', {'usuario_nombre': usuario_nombre, 'prestamos': prestamos, 'success_message':success_message})