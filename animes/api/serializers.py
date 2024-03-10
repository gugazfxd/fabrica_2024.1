from rest_framework.serializers import ModelSerializer
from ..models import Anime

class Serializer(ModelSerializer):
    class Meta: 
        model = Anime
        fields = '__all__'
