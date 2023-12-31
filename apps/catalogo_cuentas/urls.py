import uuid
from django.contrib import admin
from django.urls import path,include
from .views import (newCatalogo,
                    newCountryForm,
                    newPasivoForm,
                    newAccountForm,
                    newActivoForm,
                    newBancoForm,
                    CatalogoDetailView,
                    CatalogoDeleteView,
                    ActivoDetailView,
                    PasivoDetailView,
                    catalogUpdate,
                    GeneratePdf,
                    )
from .views import catalogoDeleteView,newCatalogo,newCountryForm,newPasivoForm,newActivoForm,CatalogoDetailView 

from .viewsets import ActivoViewSet,PasivoViewSet,CatalogoCuentasViewSet,BancoViewSet,CountryViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'activos', ActivoViewSet)
router.register(r'country', CountryViewSet)
router.register(r'pasivos', PasivoViewSet)
router.register(r'catalogo', CatalogoCuentasViewSet)
router.register(r'banco', BancoViewSet)

app_name = "catalogo_cuentas"

urlpatterns = [
    ##############################
    # 
    ################################

    path('rest/', include(router.urls)),

    path('', newCatalogo, name = 'catalogo'),
    
    path('newCountry/', newCountryForm, name = 'response'),
    path('newPasivo/',newPasivoForm , name = 'response'),
    path('newActivo/', newActivoForm, name = 'response'),
    path('newAccount/', newAccountForm, name = 'response'),
    path('newBank/', newBancoForm, name = 'response'),
    
    path('activo/<int:pk>',ActivoDetailView.as_view()),
    path('pasivo/<int:pk>',PasivoDetailView.as_view()),
    
    
    path('<slug:id>/delete',catalogoDeleteView),
    path('<slug:id_catalogo>/view',CatalogoDetailView.as_view()),
    path('<slug:myid>/edit',catalogUpdate),
    path('pdf/', GeneratePdf.as_view(),name='pdf'),

]

