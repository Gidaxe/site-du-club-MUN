# Generated by Django 4.0.3 on 2022-06-01 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0002_alter_membre_generation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membre',
            name='generation',
            field=models.CharField(choices=[], max_length=100),
        ),
    ]
