# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-21 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prepaid_agreements', '0001_add_prepaid_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='prepaidproduct',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
