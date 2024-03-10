from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from..models import Anime
from serializers import Serializer
import requests

class AppViewSet(ModelViewSet):
    def list(self,request):
        anime_name = request.query_params.get('name', 'Solo Leveling') #O query params é outra forma de passar valores pela url mas, dessa forma ao invés de passar apenas um parâmetro por rota, podemos passar vários
        anime_search_url = f"https://api.jikan.moe/v4/anime?q={anime_name}"
        
        response = requests.get(anime_search_url)
        anime_data = response.json()
        
        mal_id = anime_data['data'][0]['mal_id']
        num_episodes = anime_data['data'][0]['num_episodes']
        
        anime_staff_url = f"https://api.jikan.moe/v4/anime/{mal_id}/staff"
        staff_response = requests.get(anime_staff_url)
        staff_data = staff_response.json()
        
        studio = staff_data['data'][0]['studio']
        
        anime = Anime.objects.create(
            nome=anime_name,
            numero_episodios=num_episodes,
            studio=studio
        )

        meu_serializer = Serializer(anime)
        return Response(meu_serializer.data)