from django.db import models
from general.models import Generation


class BigSlider(models.Model):
    img_url = models.URLField(blank=True, null=True)
    img_upload = models.ImageField(blank=True, null=True, upload_to='images/')
    titre_slide = models.CharField(max_length=50)
    taille_titre_slide1 = models.PositiveIntegerField(blank=True, null=True)
    texte_slide = models.TextField(max_length=2000)
    taille_texte_slide = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.titre_slide}"

    def set_default(self):
        self.titre_slide = 'Titre'
        self.texte_slide = "Texte"


class Membre(models.Model):
    generations = [(f'{gen.Nom_de_la_Génération}', f'{gen.Nom_de_la_Génération}') for gen in Generation.objects.all()]
    img_url = models.URLField(blank=True, null=True)
    img_upload = models.ImageField(blank=True, null=True, upload_to='images/')
    generation = models.CharField(max_length=100, choices=generations)
    Nom = models.CharField(max_length=25)
    description_perso = models.TextField(max_length=4000)

    def __str__(self):
        return f"{self.Nom}"


class PresentationClub(models.Model):
    titre = models.CharField(max_length=100)
    taille_titre = models.PositiveIntegerField(blank=True, null=True)
    texte = models.TextField(max_length=4000)
    taille_texte = models.PositiveIntegerField(blank=True, null=True)

    def set_default(self):
        self.titre = 'Titre'
        self.texte = 'Texte'

