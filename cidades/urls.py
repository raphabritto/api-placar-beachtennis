from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import *


router = DefaultRouter()
router.register('paises', PaisesViewSet, basename='Paises')
router.register('estados', EstadosViewSet, basename='Estados')
router.register('cidades', CidadesViewSet, basename='Cidades')

urlpatterns = [
    path('', include(router.urls))
]