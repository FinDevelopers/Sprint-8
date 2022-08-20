from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TarjetaForm
from datetime import datetime, timedelta
import random
from django.urls import reverse
# Create your views here.
@login_required(login_url='/login/')
def tarjetas(request):
    usuario_nombre = request.user.get_full_name()
    #tarjetas = Tarjeta.objects.all().filter(card_customer=7)
    tarjetas = request.user.cliente.tarjetas.all()
    success_message = ''
    if request.GET.get('status','') == 'success':
        success_message = 'Tarjeta añadida con éxito'
    return render(request, 'Tarjetas/tarjetas.html', {"usuario_nombre": usuario_nombre, "tarjetas": tarjetas, "success_message": success_message})

@login_required(login_url='/login/')
def formulario(request):
    usuario_nombre = request.user.get_full_name()
    form = TarjetaForm()
    if(request.method == "POST"):
        form= TarjetaForm(request.POST)
        if(form.is_valid()):
            tarjeta = form.save()
            tarjeta.customer = request.user.cliente
            tarjeta.card_from_date = datetime.now().strftime("%Y-%m-%d")
            tarjeta.card_expiration_date = (datetime.now() + timedelta(weeks=261)).strftime("%Y-%m-%d")
            tarjeta.card_number = random.randint(100000000000000, 9999999999999999)
            tarjeta.card_cvv = random.randint(100,999)
            tarjeta.save()
            return redirect(reverse('Tarjetas')+'?status=success')

    return render(request, 'Tarjetas/formulario.html', {"usuario_nombre": usuario_nombre, "form": form})