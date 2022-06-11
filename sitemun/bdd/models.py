from django.db import models


class BddFile(models.Model):
    img_url = models.URLField(blank=True, null=True)
    img_upload = models.ImageField(default='', blank=True, null=True)
    titre = models.CharField(max_length=100)
    description = models.TextField(max_length=4000)
    taille_texte = models.PositiveIntegerField(blank=True, null=True)
    fichier = models.FileField(default='', upload_to='fichiers/%Y/%m/%D')

    def __str__(self):
        return f"{self.titre}"

