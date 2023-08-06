from django.shortcuts import render
from django.views.generic import View,DetailView,DeleteView
from apps.catalogo_cuentas.models import CatalogoCuentas
from .models import User
# Create your views here.

class UserDetailView(DetailView):
    model = User
    template_name = 'user_perfil.html'
    context_object_name = 'user'


