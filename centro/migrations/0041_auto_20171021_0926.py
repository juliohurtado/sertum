# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-21 14:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('centro', '0040_auto_20171021_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knowledge',
            name='center',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='knowledge', to='centro.Center'),
        ),
    ]