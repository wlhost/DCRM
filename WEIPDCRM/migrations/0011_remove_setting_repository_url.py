# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-16 07:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WEIPDCRM', '0010_version_control_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='repository_url',
        ),
    ]