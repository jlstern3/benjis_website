# Generated by Django 2.2 on 2022-02-18 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_auto_20220217_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='user_note',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.User'),
        ),
    ]