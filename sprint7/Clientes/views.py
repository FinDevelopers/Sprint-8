from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
#def index(request):
@login_required(login_url='/login/')
def index(request):
    usuario_nombre = request.user.get_full_name()
    movimientos = request.user.cliente.movimientos.all().order_by('-movement_id')[:10]
    saldo = request.user.cliente.cuentas.get(account_type = 3).saldo_con_formato()
    return render(request, 'Clientes/index.html', {"usuario_nombre": usuario_nombre, "saldo": saldo, "movimientos": movimientos})
    
    