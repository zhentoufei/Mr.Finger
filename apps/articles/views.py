# coding:utf-8
from django.shortcuts import render
from django.views.generic import View
from .models import Article
# Create your views here.


class ArticleView(View):
    '''
    获取主页的文章
    '''
    def get(self, request):
        all_article = Article.objects.all()
        return render(request, 'index.html', {
            'all_article': all_article
        })