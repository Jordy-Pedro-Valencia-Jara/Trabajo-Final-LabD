# Generated by Django 3.0.8 on 2020-07-28 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comelona', '0004_auto_20200723_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platillo',
            name='Brev',
            field=models.CharField(max_length=100),
        ),
    ]