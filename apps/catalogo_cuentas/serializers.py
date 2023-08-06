from rest_framework import serializers

from .models import Activo,Pasivo,CatalogoCuentas, TypeAccount ,SubTypeAccount,Country,Banco,Country

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

class CatalogoCuentasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CatalogoCuentas
        fields = ['id_catalogo','country','date','type_catalog','banco','name','activos','pasivos','patrimonio_neto','gastos','ingresos','saldo_intermediario',]

