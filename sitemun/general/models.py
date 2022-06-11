from django.db import models
from colorfield.fields import ColorField


class NavBar(models.Model):
    logo = models.ImageField(default='', blank=True, null=True, upload_to='images/')
    taille_texte = models.PositiveIntegerField(blank=True, null=True)
    taille_barre = models.PositiveIntegerField(blank=True, null=True)
    couleur = ColorField(default='#55d6aa')
    highlights = ColorField(default="#f54242")

    def set_default(self):
        pass


class Background(models.Model):
    image_upload = models.ImageField(default='', blank=True, null=True, upload_to='images/')
    color = ColorField(default='#5EFF93')

    def __str__(self):
        return 'Background'

    def set_default(self):
        self.image_upload = ''


class Footer(models.Model):
    address1 = models.EmailField()
    address2 = models.EmailField()
    address3 = models.EmailField()
    couleur = ColorField(default='#55d6aa')

    def __str__(self):
        return 'Addresses'

    def set_default(self):
        self.address1 = 'exemple@lyceemermozdakar.org'
        self.address2 = 'exemple@lyceemermozdakar.org'
        self.address3 = 'exemple@lyceemermozdakar.org'


class Generation(models.Model):
    Nom_de_la_Génération = models.CharField(max_length=100, default='')
    Citation = models.TextField(max_length=2000, help_text='''Coucou, ici Axel codeur de la première génération ( les OGs !). J'espere vraiment que vous appréciez le site et que le Club prospère. Les conférences MUN sont vraiment des expériences géniales,
        pourvus que vous jouiez le jeu et vous jetiez à l'eau. Pour ma part, je vous souhaite de vous épanouir pleinement
         dans ce Club et d'y passer de belles années ! Bonne chance à tous ! Même si je sais que vous n'en aurez pas besoin, puisque
          je suis intimement convaincu que tous les élèves du Club MUN (sans exceptions) sont BRILLANTS XD''')
    photo_de_groupe = models.ImageField(default='images/MUNTEAM.jpg', upload_to='images/')

    def __str__(self):
        return f'{self.Nom_de_la_Génération}'

    def set_default(self):
        self.Nom_de_la_Génération = ' '
        self.Citation = " "

# TODO: Make as many things as possible customizable (pictures, section titles, etc...), team-up with sasha.
# TODO: specify tag-type in front of every field (h1/h2/p/etc..)
