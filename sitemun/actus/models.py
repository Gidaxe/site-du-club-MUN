from django.db import models


class NewsBox(models.Model):
    img_url = models.URLField(blank=True, null=True, max_length=2080)
    img_upload = models.ImageField(default='', blank=True, null=True, upload_to='images/')
    titre = models.CharField(max_length=100)
    taille_titre = models.PositiveIntegerField(blank=True, null=True)
    texte = models.TextField(max_length=4000)
    taille_texte = models.PositiveIntegerField(blank=True, null=True)
    bouton_vert = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.titre}"
