from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import View,DetailView,DeleteView
from apps.catalogo_cuentas.models import CatalogoCuentas
from .models import User
from django.urls import reverse_lazy
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

def deletePerfil(request,id):
    obj = get_object_or_404(User,id=id)
    if request.method == 'POST':
        obj.delete()
        
        return redirect('/')
    context = {
        'obj':obj
    }
    return render(request, 'user_confirm_delete.html',context)


