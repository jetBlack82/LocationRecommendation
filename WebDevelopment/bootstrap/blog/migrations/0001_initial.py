# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 04:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('member_id', models.IntegerField()),
                ('member_nickname', models.CharField(max_length=10)),
                ('rating', models.IntegerField()),
                ('restaurant_address', models.CharField(max_length=30)),
                ('restaurant_id', models.IntegerField()),
                ('restaurant_latitude', models.FloatField()),
                ('restaurant_longitude', models.FloatField()),
                ('restaurant_name', models.CharField(max_length=20)),
                ('restaurant_code', models.IntegerField()),
                ('restaurant_subcode', models.IntegerField()),
            ],
        ),
    ]
