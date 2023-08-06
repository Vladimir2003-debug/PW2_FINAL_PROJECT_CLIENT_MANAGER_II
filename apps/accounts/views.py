from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from apps.user.models import User
from apps.catalogo_cuentas.models import Country
# Create your views here.

def loginUser(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)

            return redirect("/") 

        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')    

def register(request):

    if request.method == 'POST':
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
    
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('/register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('/register/')
            else:

                user = User.objects.create_user(
                    username=username,
                    password=password1,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    country=country,
                    birthday=birthday,
                    phone_number = phone_number,
                    perfil_image="img/user.png",
                )
                
                if type_user == "cliente":
                    user.is_cliente = True
                
                if type_user == "contador":
                    user.is_contador = True

                user.save()
                userAuth = auth.authenticate(username=username,password=password1)
                auth.login(request,userAuth)
                return redirect('/')
        
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



def logout(request):
    auth.logout(request)
    return redirect('/')       