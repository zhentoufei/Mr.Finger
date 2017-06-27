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
        all_article = Article.objects.all()[:5]
        return render(request, 'index.html', {
            'all_article': all_article
        })


class ArticleDetailView(View):
    '''
    获取文章的详情
    '''
    def get(self, request, article_id):
        article = Article.objects.get(id=int(article_id))
        flag = 'detail'
        return render(request, 'detail.html', {
            "article":article,
            "flag":flag
        })
