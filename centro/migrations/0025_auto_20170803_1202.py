# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-03 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centro', '0024_auto_20170801_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knowledge',
            name='transport',
            field=models.CharField(choices=[('1', 'Transporte Público'), ('2', 'Transporte Privado')], default='0', max_length=32),
        ),
    ]