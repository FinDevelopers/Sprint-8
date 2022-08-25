from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cliente, Sucursal
from .serializers import ClienteSerializer, SucursalSerializer
from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.decorators import action

class sucursalLists( generics.ListAPIView ):
    serializer_class = SucursalSerializer
    permission_classes = []
    # GET Obtener todos los datos
    def get_queryset(self):
        return Sucursal.objects.all()


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

