# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-27 17:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0006_article_click_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=2017, verbose_name='\u6587\u7ae0\u5e74\u4efd')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article', verbose_name='\u6587\u7ae0')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0\u5e74\u4efd',
                'verbose_name_plural': '\u6587\u7ae0\u5e74\u4efd',
            },
        ),
    ]
