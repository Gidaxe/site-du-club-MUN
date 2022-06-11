from django.db import models


class TestApp(models.Model):
    titre = models.CharField(max_length=25)
    subtitle = models.CharField(max_length=25)
    piclink = models.CharField(max_length=25)

