from rest_framework import serializers
from datetime import date


from atletas.models import Atletas


class AtletasSerializer(serializers.ModelSerializer):
    idade = serializers.ReadOnlyField()
    
    class Meta:
        model = Atletas
        fields = '__all__'
        # exclude = ['atleta_id']

    # idade = serializers.SerializerMethodField()

    def get_idade(self, obj):
        return int((date.today() - obj.data_nascimento).days / 365.2425)

