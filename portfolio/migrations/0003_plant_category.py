# Generated by Django 2.2 on 2022-01-27 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20220127_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='category',
            field=models.CharField(default='fruit_veg', max_length=45),
            preserve_default=False,
        ),
    ]