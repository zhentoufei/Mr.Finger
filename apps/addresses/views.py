# coding:utf-8

from django.shortcuts import render
from .models import Address
from django.views.generic import View
# Create your views here.


class AddressView(View):
    '''
    获取访问者的Ip和时间
    '''
    def get(self,request):
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            addr = request.META['HTTP_X_FORWARDED_FOR']
            add_obj = Address.objects.create(address = addr)
        else:
            addr = request.META['REMOTE_ADDR']
            add_obj = Address.objects.create(address = addr)