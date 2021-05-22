from rest_framework import viewsets

from .serializers import AtletasSerializer
from .models import Atletas

class AtletasViewSet(viewsets.ModelViewSet):
    """
        Utilize esse endereco para gerencia o cadastro do Atleta
    """
    serializer_class = AtletasSerializer
    queryset = Atletas.objects.all()

    # http_method_names = ['DELETE',]
    