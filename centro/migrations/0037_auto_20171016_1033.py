# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-16 15:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('centro', '0036_picture_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='center',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='center', to='usuario.User'),
        ),
    ]
