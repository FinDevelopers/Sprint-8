from distutils.log import error
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm 
from .forms import RegistrationForm 
from django.contrib.auth.models import User
from Clientes.models import Cliente, Sucursal, TipoCliente
from Cuentas.models import  Cuenta, TipoCuenta
import random

# Create your views here.
def home(request):
    return render(request, 'Login/home.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None: 
            return render(request, 'Login/Login.html')
        else:
            login(request, user)
            return redirect('Index')


    return render(request, 'Login/Login.html')

def registration(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = (RegistrationForm(request.POST))
        print(form.errors)
        if form.is_valid():
            user = form.save()
            user.first_name = request.POST.get('name')
            user.last_name = request.POST.get('surname')
            user.email = request.POST.get('mail')
            user.save()

            cliente = Cliente()
            cliente.customer_name = request.POST.get('name')
            cliente.customer_surname = request.POST.get('surname')
            cliente.customer_dni = request.POST.get('dni')
            cliente.dob = request.POST.get('dob')
            cliente.branch = Sucursal.objects.get(pk=request.POST.get('branch'))
            cliente.client_type = TipoCliente.objects.get(pk=request.POST.get('client_type'))
            cliente.user = user
            cliente.save()

            cuenta = Cuenta()
            cuenta.customer = cliente
            cuenta.account_type = TipoCuenta.objects.get(pk=3)
            cuenta.balance = 0
            letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            cuenta.iban = letras[random.randint(0,len(letras))] + letras[random.randint(0,len(letras))] + str(random.randint(100000000000000,999999999999999))
            cuenta.save()
            
            login(request, user)
            return redirect('Index')
              
    return render(request, 'Login/registration.html', {'form': form})

def logout_view(request):
    logout(request)
    #Acá se puede crear un template para cuando desloguea
    return redirect('Login')
    



"""user = User()
            user.username = request.POST.get('username')
            user.password = request.POST.get('password2')
             """