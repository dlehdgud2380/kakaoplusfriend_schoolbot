# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yhbot', '0002_auto_20170901_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school_info',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='img_schoolmessage/'),
        ),
    ]