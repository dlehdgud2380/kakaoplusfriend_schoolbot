# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-17 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yhbot', '0006_school_info_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school_info',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
