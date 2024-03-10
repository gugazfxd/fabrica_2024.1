from django.db import models

# Create your models here.
class Anime(models.Model):
    nome=models.CharField(max_length=100)
    numero_episodios=models.IntegerField()
    studio=models.CharField(max_length=100)


    def __str__(self) ->str:
        return f"{self.nome}tem um total{self.numero_episodios} e foi feito por{self.studio}"


