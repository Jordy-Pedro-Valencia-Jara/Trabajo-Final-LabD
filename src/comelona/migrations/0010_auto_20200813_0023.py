# Generated by Django 3.0.8 on 2020-08-13 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comelona', '0009_auto_20200813_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]