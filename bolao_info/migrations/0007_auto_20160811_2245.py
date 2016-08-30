# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-12 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolao_info', '0006_remove_gpinfo_race_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpinfo',
            name='race_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pilotinfo',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]