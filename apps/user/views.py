from django.shortcuts import render
from django.views.generic import View,DetailView,DeleteView
from apps.catalogo_cuentas.models import CatalogoCuentas
from .models import User
# Create your views here.

def userDetailView(request,id):
    user = User.objects.get(id=id)
    if user.is_cliente:
        catalogo = CatalogoCuentas.objects.filter(cliente=user.id)
    if user.is_contador:
        catalogo = CatalogoCuentas.objects.filter(contador=user.id)

    context = {
        'catalogo':catalogo
    }

    return render(request, 'user_perfil.html',context)




