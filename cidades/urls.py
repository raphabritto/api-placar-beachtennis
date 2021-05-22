from rest_framework.routers import DefaultRouter

from .views import PaisesViewSet, EstadosViewSet, CidadesViewSet


router = DefaultRouter()
router.register('paises', PaisesViewSet, basename='Paises')
router.register('estados', EstadosViewSet, basename='Estados')
router.register('cidades', CidadesViewSet, basename='Cidades')


cidades_urls = router.urls