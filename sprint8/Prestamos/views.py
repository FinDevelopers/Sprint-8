from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from Clientes.models import Empleado, Cliente
from .forms import PrestamoForm
from .models import Prestamo
from rest_framework import  generics
from rest_framework.views import Response, status
from .serializers import PrestamoSerializer, PrestamoSerializerInsert, PrestamoSerializerDestroy, serializers




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

class prestamoSucursalLists( generics.ListAPIView ):
    serializer_class = PrestamoSerializer
    # GET Obtener todos los datos
    def get_queryset(self):
        try:
            prestamos = []
            for cliente in self.request.user.empleado.branch.clientes.all():
                prestamos = prestamos + list(cliente.prestamos.all())
            return prestamos
        except:
            return []

class prestamoLists( generics.ListAPIView ):
    serializer_class = PrestamoSerializer
    # GET Obtener todos los datos
    def get_queryset(self):
        try:
            return Prestamo.objects.filter(customer = self.request.user.cliente)
        except:
            return []

class prestamoCreate(generics.CreateAPIView):
    serializer_class = PrestamoSerializerInsert

    def post(self, request, *args, **kwargs):
        try:
            #Validando que el user sea empleado (si no es se produce una excepción)
            self.request.user.empleado
            #Formateando el monto
            monto = float(request.data.get('loan_total')) * 100

            #Setea el campo loan_total con el monto formateado
            request.data._mutable = True
            request.data['loan_total'] = monto

            #Agregandole el monto a la cuenta
            cuenta = Cliente.objects.get(pk = request.data['customer']).cuentas.get(account_type = 3)
            cuenta.recibir_prestamo(monto)


            return self.create(request, *args, **kwargs)
        except:
              return Response(serializers.Serializer().data, status=status.HTTP_400_BAD_REQUEST)


class prestamoDestroy(generics.DestroyAPIView):
    serializer_class = PrestamoSerializerDestroy

     
    def delete(self, request, pk):
        try:
            #Validando que el user sea empleado (si no es se produce una excepción)
            self.request.user.empleado

            #Obteniendo el objeto prestamo con el paramtero de la url "pk"
            prestamo = Prestamo.objects.get(pk=pk)
            serializer = PrestamoSerializerDestroy(prestamo)

            #Sacandole el monto del prestamo a al cuenta
            
            cuenta = prestamo.customer.cuentas.get(account_type = 3)
            
            cuenta.cancelar_prestamo(prestamo.loan_total)

            #Eliminando el préstamo
            prestamo.delete()

            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializers.Serializer().data, status=status.HTTP_400_BAD_REQUEST)
    
 