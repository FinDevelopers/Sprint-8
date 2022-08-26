from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Tarjeta
from Clientes.models import Cliente
from .forms import TarjetaForm
from datetime import datetime, timedelta
import random
from .serializers import TarjetaSerializer
from django.urls import reverse
from rest_framework import generics, serializers
from rest_framework.views import Response, status


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


class tarjetaLists( generics.ListAPIView ):
    serializer_class = TarjetaSerializer
    # GET Obtener todos los datos
    def get(self, request, pk):
        try:
            #Validando que el user sea empleado (si no es se produce una excepción)
            self.request.user.empleado
            
            #Obteniendo las tarjetas del cliente
            tarjetas =  Tarjeta.objects.filter(customer = Cliente.objects.get(pk=pk), card_type = 'credit' )
            
            serializer = TarjetaSerializer(tarjetas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializers.Serializer().data, status=status.HTTP_400_BAD_REQUEST)
