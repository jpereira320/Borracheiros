# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-18 17:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bolao_info', '0015_auto_20190318_1450'),
        ('bolao_bet', '0006_auto_20170129_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbet',
            name='BestLap',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='BestLap', to='bolao_info.PilotInfo'),
        ),
        migrations.AddField(
            model_name='userbet',
            name='DoD',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='DoD', to='bolao_info.PilotInfo'),
        ),
    ]