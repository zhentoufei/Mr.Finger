# coding:utf-8
from __future__ import unicode_literals

from django.db import models
from articles.models import Article
from datetime import datetime
# Create your models here.


class ArticleYear(models.Model):
    article = models.ForeignKey(Article, verbose_name=u'文章')
    year = models.IntegerField(default=datetime.now().year, verbose_name=u'文章年份')

    class Meta:
        verbose_name = u'文章年份'
        verbose_name_plural = verbose_name
