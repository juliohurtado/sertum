# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-25 14:27
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('centro', '0022_auto_20170724_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knowledge',
            name='group_type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('0', 'Niños'), ('1', 'Adultos'), ('2', 'Adultos Mayores')], default='0', max_length=32),
        ),
        migrations.AlterField(
            model_name='knowledge',
            name='transport',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('0', 'Transporte Público'), ('1', 'Transporte Privado')], default='0', max_length=32),
        ),
        migrations.AlterField(
            model_name='poll',
            name='group_type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('0', 'Niños'), ('1', 'Adultos'), ('2', 'Adultos Mayores')], default='0', max_length=32),
        ),
        migrations.AlterField(
            model_name='poll',
            name='transport',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('0', 'Transporte Público'), ('1', 'Transporte Privado')], default='0', max_length=32),
        ),
    ]
