# Generated by Django 3.2.5 on 2021-07-13 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0014_canteen_production_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-display_date'], 'verbose_name': 'article de blog', 'verbose_name_plural': 'articles de blog'},
        ),
    ]
