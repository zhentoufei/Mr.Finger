# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-29 19:50
from __future__ import unicode_literals

import DjangoUeditor.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_article_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='\u5173\u4e8e')),
                ('date_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u66f4\u65b0\u65e5\u671f')),
            ],
            options={
                'verbose_name': '\u5173\u4e8e',
                'verbose_name_plural': '\u5173\u4e8e',
            },
        ),
    ]