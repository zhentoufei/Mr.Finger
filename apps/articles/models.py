# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField(max_length=64)
    def __unicode__(self):
        return self.tag_name

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = verbose_name


class Article(models.Model):
    title = models.CharField(max_length = 150)  # 博客题目
    category = models.CharField(max_length = 50, blank = True)  #博客分类 可为空
    tag = models.ForeignKey(Tag, blank=True, default='')  # 博客标签 可为空
    date_time = models.DateTimeField(auto_now_add = True)  #博客日期
    content = models.TextField(blank = True, null = True)  #博客文章正文



    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}(类别： {1})'.format(self.title, self.tag)
