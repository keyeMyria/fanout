# Generated by Django 2.1 on 2018-08-25 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PushpinStatConn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unavailable', models.BooleanField()),
                ('conn_num', models.IntegerField()),
                ('conn_id', models.CharField(max_length=100)),
                ('peer_ip', models.GenericIPAddressField()),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PushpinStatReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conn_num', models.IntegerField()),
                ('rec_msg_cnt', models.IntegerField()),
                ('sent_msg_cnt', models.IntegerField()),
                ('http_resp_sent_cnt', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PushpinStatSub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(max_length=20)),
                ('channel', models.CharField(max_length=100)),
                ('sub_cnt', models.IntegerField()),
                ('unavailable', models.BooleanField()),
            ],
        ),
    ]