from django.db import models


class AccueilIntroMun(models.Model):
    img_url1 = models.URLField(blank=True, null=True)
    img_upload1 = models.ImageField(default='', blank=True, null=True, upload_to='images/')
    img_url2 = models.URLField(blank=True, null=True)
    img_upload2 = models.ImageField(default='', blank=True, null=True, upload_to='images/')
    img_url3 = models.URLField(blank=True, null=True)
    img_upload3 = models.ImageField(default='', blank=True, null=True, upload_to='images/')
    video_url = models.URLField()
    titre = models.CharField(max_length=50)
    taille_titre = models.PositiveIntegerField(blank=True, null=True)
    texte = models.TextField(max_length=2000)
    taille_texte = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return 'Section Intro'

    def set_default(self):
        self.video_url = 'https://www.youtube.com/embed/spnd9gQ7WqU'
        self.titre = 'Titre'
        self.texte = 'Texte'



    # TODO: Custom fonts
