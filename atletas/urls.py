from rest_framework.routers import DefaultRouter

from .views import AtletasViewSet


router = DefaultRouter()
router.register('atletas', AtletasViewSet, basename='Atletas')


atletas_urls = router.urls