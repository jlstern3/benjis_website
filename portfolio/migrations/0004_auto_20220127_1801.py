# Generated by Django 2.2 on 2022-01-27 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_plant_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='days_to_harvest',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='latin_name',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='pH',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='spacing',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='sun',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='water',
            field=models.CharField(max_length=255, null=True),
        ),
    ]