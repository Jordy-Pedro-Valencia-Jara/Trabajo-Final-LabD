# Generated by Django 3.0.8 on 2020-08-13 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comelona', '0008_auto_20200813_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='total',
            field=models.IntegerField(null=True),
        ),
    ]
