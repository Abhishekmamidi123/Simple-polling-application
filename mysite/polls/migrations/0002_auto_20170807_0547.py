# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-07 05:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question',
            new_name='choices',
        ),
    ]
