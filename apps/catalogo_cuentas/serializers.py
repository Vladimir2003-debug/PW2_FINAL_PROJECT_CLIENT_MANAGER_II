from rest_framework import serializers

from .models import Activo,Pasivo,CatalogoCuentas ,Country,Banco,Country

############################################################################
# SERIALIZERS
############################################################################


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country 
        fields = ('id_country','name','description','postal_code')
class BancoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Banco
        fields = ('id_bank','name_bank','type_bank','description')
class ActivoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activo
        fields =('date','type','subtype','name_activo','saldo')

class PasivoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Pasivo 
        fields =('date','type','subtype','name_pasivo','saldo')

class CatalogoCuentasSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True) 
    banco = BancoSerializer(read_only=True) 
    activos = ActivoSerializer(read_only=True) 
    pasivos  = PasivoSerializer(read_only=True) 
    class Meta:
        model = CatalogoCuentas
        fields = "__all__" 

