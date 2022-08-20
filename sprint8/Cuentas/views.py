from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Cuenta
from .serializers import CuentaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@login_required(login_url='/login/')
def movimientos(request):
    usuario_nombre = request.user.get_full_name()
    #tarjetas = Tarjeta.objects.all().filter(card_customer=7)
    movimientos = request.user.cliente.movimientos.all().order_by('-movement_datetime')
    return render(request, 'Cuentas/movimientos.html', {"usuario_nombre": usuario_nombre, "movimientos": movimientos})

class cuentaLists( APIView ):
    # GET Obtener todos los datos
    def get(self, request):
        cuentas = Cuenta.objects.all()
        serializer = CuentaSerializer(cuentas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST Crear un nuevo registro
    def post(self, request):
        serializer = CuentaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class cuentaDetail( APIView ):
    # GET Obtener un registro especifico
    def get(self, request, pk):
        cuenta = Cuenta.objects.get(pk=pk)
        serializer = CuentaSerializer(cuenta)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # PUT Actualizar un registro específico
    def put(self, request, pk):
        cuenta = Cuenta.objects.get(pk=pk)
        serializer = CuentaSerializer(cuenta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE Eliminar un registro específico
    def delete(self, request, pk):
        cuenta = Cuenta.objects.get(pk=pk)
        cuenta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)