# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-17 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups_manager', '0003_0_5_0_rename_reverse_relations_with_vars'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmember',
            name='expiration_date',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
