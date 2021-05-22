from rest_framework.routers import DefaultRouter

from .views import TorneiosViewSet


router = DefaultRouter()
router.register('torneios', TorneiosViewSet, basename='Torneios')


torneios_urls = router.urls