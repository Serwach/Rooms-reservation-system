# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 16:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_auto_20171112_0926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='surname',
            new_name='password',
        ),
    ]