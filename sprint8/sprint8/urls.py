"""sprint7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Clientes import views as clientes
from Login import views as login
from Prestamos import views as prestamos
from Tarjetas import views as tarjetas
from Cuentas import views as cuentas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', clientes.index, name="Index"),
    path('formularios-prestamo/', prestamos.formulario, name="Formulario"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('logout/', login.logout_view , name="Logout"),
    path('login/', login.login_view , name="Login"),
    path('registration/', login.registration , name="Registration"),
    path('', login.home , name="Home"),
    path('prestamos/', prestamos.prestamos, name="Prestamos"),
    path('tarjetas/', tarjetas.tarjetas, name="Tarjetas"),
    path('formulario-tarjeta/', tarjetas.formulario, name="Formulario-tarjeta"),
    path('cuentas/', cuentas.movimientos, name="Movimientos"),
    path('api/cuentas/', cuentas.cuentaLists.as_view(), name="API-Cuentas"),
    path('api/cuentas/<int:pk>/', cuentas.cuentaDetail.as_view(), name="API-Cuenta"),
    
]
