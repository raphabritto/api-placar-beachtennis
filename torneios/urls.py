from rest_framework.routers import DefaultRouter

from .views import TorneiosViewSet, NivelCategoriasViewSet


router = DefaultRouter()
router.register('torneios', TorneiosViewSet, basename='Torneios')
router.register('nivelcategorias', NivelCategoriasViewSet, basename='NivelCategorias')


torneios_urls = router.urls