# coding:utf-8
from django.shortcuts import render
from django.views.generic import View
from .models import UserAbout
# Create your views here.


def page_not_found(request):
    from django.shortcuts import render_to_response
    response = render_to_response('error404.html',{})
    response.status_code=404
    return response


class UserAboutView(View):
    '''
    取出关于用户信息
    '''
    def get(self, request):
        about = UserAbout.objects.all()[0]
        flag = 'about'
        return render(request, 'about.html',{
            "about":about,
            'flag':flag
        })
