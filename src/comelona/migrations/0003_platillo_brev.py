# Generated by Django 3.0.8 on 2020-07-23 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comelona', '0002_remove_platillo_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='platillo',
            name='Brev',
            field=models.TextField(default='Ingredientes'),
        ),
    ]
