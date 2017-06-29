# coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

from DjangoUeditor.models import UEditorField
from datetime import datetime


# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    birday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gender = models.CharField(choices=(("male", u"男"), ("female", u"女")), default="female", max_length=20)
    address = models.CharField(max_length=100, default=u"")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    detail = models.TextField(max_length=1000, blank=True)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class UserAbout(models.Model):
    about = UEditorField(verbose_name=u'关于', width=900, height=500, imagePath="ueditor/%Y/%m",
                         filePath="ueditor/%Y/%m", blank=True, default="")
    date_time = models.DateTimeField(verbose_name=u'更新日期', default=datetime.now)  # 更改日期

    class Meta:
        verbose_name = u"关于"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'关于我'
