from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# from .models import Paises
# from .serializers import PaisesSerializer


# class PaisesViewSet(viewsets.ModelViewSet):
#     serializer_class = PaisesSerializer
#     queryset = Paises.objects.all()
#     # permission_classes = (IsAuthenticated,)
#     # authentication_classes = (TokenAuthentication,)
