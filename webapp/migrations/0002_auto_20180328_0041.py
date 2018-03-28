# Generated by Django 2.0.3 on 2018-03-28 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='herramienta',
            name='informacion_tecnica',
        ),
        migrations.AddField(
            model_name='herramienta',
            name='descripcion_funcional',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='herramienta',
            name='integracion_con_lms',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='herramienta',
            name='sistemas_operativos',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='herramienta',
            name='version',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='Informacion_Tecnica',
        ),
    ]