from django.db import models


class Pattes(models.Model):
    nom = models.CharField(max_length=200)
    ingredients = models.TextField(max_length=600)
    prix = models.FloatField(default=None)
    vegetarienne = models.BooleanField(default=False)
    bio = models.BooleanField(default=False)

    # gerer l'affichage en fonction du nom
    def __str__(self):
        return self.nom
