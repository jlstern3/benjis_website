# Generated by Django 2.2 on 2022-04-07 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0022_plant_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='img',
        ),
    ]