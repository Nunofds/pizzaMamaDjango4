from django.db import models


class Pizza(models.Model):
    nom = models.CharField(max_length=200)
    ingredients = models.TextField(max_length=400)
    prix = models.FloatField(default=0)
    vegetarienne = models.BooleanField(default=False)

    # gerer l'affichage en fonction du nom
    def __str__(self):
        return self.nom
