# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
