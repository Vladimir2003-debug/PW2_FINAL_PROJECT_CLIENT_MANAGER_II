from .models import Activo,Pasivo,CatalogoCuentas,Banco,Country
from .serializers import ActivoSerializer,PasivoSerializer,CatalogoCuentasSerializer,BancoSerializer,CountrySerializer
from rest_framework import viewsets

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer   
class ActivoViewSet(viewsets.ModelViewSet):
    queryset = Activo.objects.all()
    serializer_class = ActivoSerializer 

class PasivoViewSet(viewsets.ModelViewSet):
    queryset = Pasivo.objects.all()
    serializer_class = PasivoSerializer 

class CatalogoCuentasViewSet(viewsets.ModelViewSet):
    queryset = CatalogoCuentas.objects.all()
    serializer_class = CatalogoCuentasSerializer 

class BancoViewSet(CatalogoCuentasViewSet):
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer 
