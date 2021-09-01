# Generated by Django 3.2.6 on 2021-08-30 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0025_auto_20210830_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teledeclaration',
            name='source',
        ),
        migrations.AddField(
            model_name='teledeclaration',
            name='diagnostic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.diagnostic', verbose_name='diagnostic'),
        ),
    ]
