# Generated by Django 3.0.8 on 2020-07-29 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comelona', '0005_auto_20200728_0038'),
    ]

    operations = [
        migrations.CreateModel(
            name='chef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('las_name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='platillo',
            name='chef_cocinero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comelona.chef'),
        ),
    ]