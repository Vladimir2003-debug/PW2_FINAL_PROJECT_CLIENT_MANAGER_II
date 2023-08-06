from django.shortcuts import (render,HttpResponse,redirect,get_object_or_404)
from .forms import (RawCatalogoForm,
                    RawCuentaForm,
                    RawCountryForm,
                    RawActivoForm,
                    RawPasivoForm,
                    RawBancoForm)
from .models import (CatalogoCuentas,
                    Country,
                    Pasivo,
                    Activo,
                    Cuenta,
                    Banco)
                    
from django.views.generic import View,DetailView,UpdateView,DeleteView
from django.template.loader import get_template
from .utils import render_to_pdf #created in step 4
from datetime import date
from django.contrib.auth import authenticate, login
from apps.user.models import User

from django.urls import reverse_lazy


# Create your views here.

############################################################
# VIEWS
class CatalogoDetailView(DetailView):
    model = CatalogoCuentas
    template_name = 'view/catalogo_detail.html'
    context_object_name = 'catalogo'
    pk_url_kwarg = 'id_catalogo'

class CatalogoDeleteView(DeleteView):
    model = CatalogoCuentas
    template_name = 'delete/catalogo_delete.html'
    success_url = reverse_lazy('')
    pk_url_kwarg = 'id_catalogo'

    
class ActivoDetailView(DetailView):
    model = Activo
    template_name = 'view/activo_detail.html'
    context_object_name = 'activo'
    pk_url_kwarg = 'id_activo'

class PasivoDetailView(DetailView):
    model = Pasivo
    template_name = 'view/pasivo_detail.html'
    context_object_name = 'pasivo'
    pk_url_kwarg = 'id_pasivo'

#########################################################
# NEWS

def newCatalogo(request):

    if request.method=='POST':
        pasivos = request.POST.getlist('pasivos')
        activos = request.POST.getlist('activos')
        cuentas = request.POST.getlist('cuentas')

        country = request.POST['country']
        type_catalogo= request.POST['type_catalogo']
        patrimonio_neto = request.POST['patrimonio_neto']
        gastos = request.POST['gastos']
        banco = request.POST['banco']
        ingresos = request.POST['ingresos']
        saldo_intermediario = request.POST['saldo_intermediario']
        dateToday = date.today()
        name = request.POST['name']
        cliente = request.POST['cliente']

        print("CUENTAS")
        print(activos)
        print(pasivos)
        print(cuentas)

        print(pasivos)
        if name is not None:

            contador = User.objects.get(username=request.user)

            catalogo = CatalogoCuentas.objects.create(
                country_id=country,
                name=name,
                date=dateToday,
                type_catalog=type_catalogo,
                banco_id=banco,
                patrimonio_neto=patrimonio_neto,
                gastos=gastos,
                ingresos=ingresos,
                saldo_intermediario=saldo_intermediario,
                cliente=cliente,
                contador=contador.id,
            )

            for a in activos:
                catalogo.activos.add(a)
            for p in pasivos:
                catalogo.pasivos.add(p)
            for c in cuentas:
                catalogo.cuentas_de_orden.add(c)
            
            catalogo.save()
            return redirect('/user/'+str(contador.id))

    form = RawCatalogoForm()
    country = Country.objects.all()
    banco = Banco.objects.all()
    cliente = User.objects.filter(is_cliente=True)

    activos = Activo.objects.all()
    pasivos = Pasivo.objects.all()
    cuentas = Cuenta.objects.all()

    context = {
        'form': form,
        'country':country,
        'banco':banco,
        'cliente':cliente,
        'activo':activos,
        'pasivo':pasivos,
        'cuentas':cuentas,
    }

    return render(request, 'new/newCatalog.html',context) 

def newCountryForm(request):
    if request.method=='POST':
        name = request.POST['name']
        description = request.POST['description']

        if name is not None:
            Country.objects.create(name=name, description=description)
            return redirect('/')
    
    form = RawCountryForm()
    context = {
        'form': form,
    }
    
    return render(request, 'new/newCountry.html',context) 

def newBancoForm(request):
    if request.method=='POST':
        name = request.POST['name']
        description = request.POST['description']

        if name is not None:
            Country.objects.create(name=name, description=description)
            return redirect('/')
    
    form = RawBancoForm()
    context = {
        'form': form,
    }
    
    return render(request, 'new/newBanco.html',context) 


def newPasivoForm(request):
    if request.method=='POST':
        name_pasivo = request.POST['name']
        saldo_pasivo = request.POST['saldo']
        type_pasivo= request.POST['type']
        subtype_pasivo = request.POST['subtype']
        date_pasivo = date.today()
        
        if name_pasivo is not None:
            Pasivo.objects.create( date=date_pasivo,name_pasivo=name_pasivo, saldo=saldo_pasivo, type=type_pasivo, subtype=subtype_pasivo)
            return redirect('/')
    
    form = RawPasivoForm()
    context = {
        'form': form,
    }
    return render(request, 'new/newPasivo.html',context) 

def newActivoForm(request):
    if request.method=='POST':
        name_activo = request.POST['name']
        saldo_activo = request.POST['saldo']
        type_activo = request.POST['type']
        subtype_activo = request.POST['subtype']
        date_activo = date.today()
        
        if name_activo is not None:
            Activo.objects.create( date=date_activo,name_activo=name_activo, saldo=saldo_activo, type=type_activo, subtype=subtype_activo)
            return redirect('/')
    
    form = RawActivoForm()
    context = {
        'form': form,
    }
    return render(request, 'new/newActivo.html',context) 

def newAccountForm(request):
    if request.method == 'POST':
        type_account = request.POST["type_account"]
        pasivo = request.POST["pasivo"]
        activo = request.POST["activo"]
        name_account = request.POST["name"]
        type_account = request.POST["type_account"]
        date_account = date.today()
        saldo = activo-pasivo
        
        if name_account is not None:
            cuenta=Cuenta.objects.create(
                date=date_account,
                name=name_account,
                type_account=type_account,
                pasivos=pasivo,
                activos=activo,
            )
            if saldo < 0:
                cuenta.mov_deudor = True
            else:
                cuenta.mov_acreedor = True
            cuenta.save()

            return redirect("/")

    form = RawCuentaForm()
    context = {
        'form': form,
    }
    return render(request, 'new/newAccount.html',context) 

##########################################################
# Edit 

def catalogUpdate(request,myid):
    catalogo = CatalogoCuentas.objects.get(id_catalogo=myid)

    if request.method=='POST':
        pasivos = request.POST.getlist('pasivos')
        activos = request.POST.getlist('activos')
        cuentas = request.POST.getlist('cuentas')
        country = request.POST['country']
        type_catalogo= request.POST['type_catalogo']
        patrimonio_neto = request.POST['patrimonio_neto']
        gastos = request.POST['gastos']
        banco = request.POST['banco']
        ingresos = request.POST['ingresos']
        saldo_intermediario = request.POST['saldo_intermediario']
        dateToday = date.today()
        name = request.POST['name']
        cliente = request.POST['cliente']

        
        if name is not None:
            catalogo.country_id = country
            catalogo.name=name
            catalogo.type_catalog=type_catalogo
            catalogo.banco_id=banco
            catalogo.patrimonio_neto=patrimonio_neto
            catalogo.gastos=gastos
            catalogo.ingresos=ingresos
            catalogo.saldo_intermediario=saldo_intermediario
            catalogo.cliente=cliente
            catalogo.date = dateToday
            catalogo.save()
            user = User.objects.get(username=request.user)
            return redirect('/user/'+str(user.id))

    form = RawCatalogoForm()

    country = Country.objects.all()
    banco = Banco.objects.all()
    cliente = User.objects.filter(is_cliente=True)

    catalogo = CatalogoCuentas.objects.get(id_catalogo=myid)

    context = {
        'form': form,
        'country':country,
        'banco':banco,
        'cliente':cliente,
        'catalogo':catalogo
    }    
    
    return render(request, 'new/newCatalog.html', context)



class GeneratePdf(View): 
    def get(self, request, *args, **kwargs):
        pdf = request.GET["pdf"]

        catalogo = CatalogoCuentas.objects.get(id_catalogo=pdf)

        context = {
            "catalogo" : catalogo
        } 

        pdf = render_to_pdf('view/catalogo_detail.html',context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Catalogo_%s.pdf" %(12341231)
            content = "inline; filename=%s" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename=%s" %(filename) 
            response['Content-Disposition'] = content
            return response
        return HttpResponse('No Found')
    