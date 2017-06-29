# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Address(models.Model):
    address = models.CharField(max_length=50, verbose_name=u'访问IP')
    date_time = models.DateTimeField(auto_now_add=True, verbose_name=u'访问时间')

    class Meta:
        verbose_name = u'访问记录'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.address
