# Generated by Django 4.1.2 on 2022-11-28 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='descripcion',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.CharField(max_length=500),
        ),
    ]
