# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-27 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20170627_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='click_number',
            field=models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u6570'),
        ),
    ]
