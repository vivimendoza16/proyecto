# Generated by Django 2.0.3 on 2018-03-30 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_archivo_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivo',
            name='nombre',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='archivo',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]