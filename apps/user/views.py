from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.views.generic import View,DetailView,DeleteView
from django.contrib.auth.models import auth
from apps.catalogo_cuentas.models import CatalogoCuentas,Country
from .models import User
from django.urls import reverse_lazy
# Create your views here.

def userDetailView(request,id):
    user = User.objects.get(id=id)
    if user.is_cliente:
        catalogo = CatalogoCuentas.objects.filter(cliente=user.id)
    if user.is_contador:
        catalogo = CatalogoCuentas.objects.filter(contador=user.id)
    country = Country.objects.get(id_country=user.country)
    context = {
        'catalogo':catalogo,
        'country':country

    }

    return render(request, 'user_perfil.html',context)

def userEdit(request,id):


    if request.method == 'POST':
        user = User.objects.get(id=id)
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        country = request.POST['country_id']

        birthday = request.POST['birthday']
        phone_number = request.POST['phone_number']
        type_user = request.POST['type_user']
        gender = request.POST['gender']
        address = request.POST['address']
        description = request.POST['description']

        if password1==password2:
                user.username=username
                user.password=password1
                user.email=email
                user.first_name=first_name
                user.last_name=last_name
                user.country=country
                user.birthday=birthday
                user.phone_number = phone_number
                user.address=address
                user.description=description
                user.gender=gender
                
                if type_user == "cliente":
                    user.is_cliente = True
                
                if type_user == "contador":
                    user.is_contador = True

                user.save()

                auth.login(request,user)

                return redirect('/user/' + str(user.id))
        
        else:
            messages.info(request,'password not matching..')    
            return redirect('/register/')
        return redirect('/')

    else:
        queryset = Country.objects.all()
        context = {
            'country':queryset
            }

        return render(request,'register.html',context)


def deletePerfil(request,id):
    obj = get_object_or_404(User,id=id)
    if request.method == 'POST':
        obj.delete()
        
        return redirect('/')
    context = {
        'obj':obj
    }
    return render(request, 'user_confirm_delete.html',context)


