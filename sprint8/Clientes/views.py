from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cliente, Direccion, Sucursal
from .serializers import ClienteSerializer, SucursalSerializer, DireccionUpdateSerializer
from rest_framework.response import Response
from rest_framework import  generics, serializers
from rest_framework.views import status


# Create your views here.
#def index(request):
@login_required(login_url='/login/')
def index(request):
    usuario_nombre = request.user.get_full_name()
    movimientos = request.user.cliente.movimientos.all().order_by('-movement_id')[:10]
    saldo = request.user.cliente.cuentas.get(account_type = 3).saldo_con_formato()
    return render(request, 'Clientes/index.html', {"usuario_nombre": usuario_nombre, "saldo": saldo, "movimientos": movimientos})
    

class ClienteList(generics.ListAPIView):
    serializer_class = ClienteSerializer
    def get_queryset(self):
        try:
            return Cliente.objects.filter(pk = self.request.user.cliente.customer_id)
        except:
            return []

class sucursalLists( generics.ListAPIView ):
    serializer_class = SucursalSerializer
    permission_classes = []
    # GET Obtener todos los datos
    def get_queryset(self):
        return Sucursal.objects.all()

class direccionUpdateFromCliente( generics.UpdateAPIView ):
    serializer_class = DireccionUpdateSerializer
    
    def put(self, request, *args, **kwargs):
        try:
            #Obteniendo la direccion asociadoa al cliente
            direccion = Cliente.objects.get(pk = self.request.user.cliente.customer_id).direcciones.first()
            serializer = DireccionUpdateSerializer(direccion)
            
            #Acutalizando los campos de la direccion y guardandolos en la bd
            direccion.address_street = request.data['address_street']
            direccion.address_number = request.data['address_number']
            direccion.address_city = request.data['address_city']
            direccion.address_province = request.data['address_province']
            direccion.address_country = request.data['address_country']
            direccion.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializers.Serializer().data, status=status.HTTP_400_BAD_REQUEST)
        


class direccionUpdateFromEmpleado( generics.UpdateAPIView ):
    serializer_class = DireccionUpdateSerializer
    
    def put(self, request, pk, *args, **kwargs):
        try:
            #Validando que el user sea empleado (si no es se produce una excepción)
            self.request.user.empleado

            #Obteniendo la direccion asociadoa al cliente
            direccion = Direccion.objects.get(pk =pk)
            serializer = DireccionUpdateSerializer(direccion)
            
            #Acutalizando los campos de la direccion y guardandolos en la bd
            direccion.address_street = request.data['address_street']
            direccion.address_number = request.data['address_number']
            direccion.address_city = request.data['address_city']
            direccion.address_province = request.data['address_province']
            direccion.address_country = request.data['address_country']
            direccion.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializers.Serializer().data, status=status.HTTP_400_BAD_REQUEST)