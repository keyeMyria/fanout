# Generated by Django 2.1 on 2018-08-27 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20180827_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pushpinstatreport',
            name='time_stamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='pushpinstatsub',
            name='time_stamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
