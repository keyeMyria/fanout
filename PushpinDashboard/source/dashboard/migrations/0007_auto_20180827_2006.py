# Generated by Django 2.1 on 2018-08-27 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20180827_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='channel_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]