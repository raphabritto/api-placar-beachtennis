"""api_beachtennis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from atletas.views import *
# from torneios.views import TorneiosViewSet, NivelCategoriasViewSet, GeneroCategoriasViewSet
from torneios.views import *
from cidades.views import *

# from paises.urls import paises_urls
# from cidades.urls import cidades_urls
# from atletas.urls import atletas_urls
# from torneios.urls import torneios_urls

route = routers.DefaultRouter()

route.register(r'atletas', AtletasViewSet, basename='Atletas')
route.register(r'torneios', TorneiosViewSet, basename='Torneios')
route.register(r'nivelcategorias', NivelCategoriasViewSet, basename='NivelCategorias')
route.register(r'generocategorias', GeneroCategoriasViewSet, basename='GeneroCategorias')
route.register(r'tiposcategorias', TipoCategoriasViewSet, basename='TipoCategorias')
route.register(r'torneiocategorias', TorneioCategoriasViewSet, basename='TorneioCategorias')
route.register(r'equipes', EquipesViewSet, basename='Equipes')
route.register(r'jogos', JogosViewSet, basename='Jogos')
route.register(r'placar', PlacarViewSet, basename='Placar')
route.register(r'paises', PaisesViewSet, basename='Paises')
route.register(r'estados', EstadosViewSet, basename='Estados')
route.register(r'cidades', CidadesViewSet, basename='Cidades')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    # path('', include(cidades_urls)),
    # path('', include(atletas_urls)),
    # path('', include(torneios_urls)),
    path('api-token-auth/', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
