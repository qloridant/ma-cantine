# Generated by Django 4.0.3 on 2022-05-10 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0068_merge_20220506_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='source',
            field=models.CharField(blank=True, choices=[('WEBINAIRE', 'Webinaire'), ('WEB_SEARCH', 'Recherche web'), ('INSTITUTION', 'Communication institutionnelle (DRAAF, association régionale)'), ('WORD_OF_MOUTH', 'Bouche à oreille'), ('SOCIAL_MEDIA', 'Réseaux sociaux'), ('OTHER', 'Autre (spécifiez)')], max_length=255, null=True, verbose_name='Comment est-ce que la personne a connu ma cantine ?'),
        ),
    ]
