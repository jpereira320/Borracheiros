# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-29 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolao_bet', '0005_usertotalpoints_gprix'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbet',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userbet',
            name='repeated',
            field=models.BooleanField(default=False),
        ),
    ]
