# coding:utf-8
from django.shortcuts import render
from django.views.generic import View
from .models import Article, About
# Create your views here.


class ArticleView(View):
    '''
    获取主页的文章
    '''
    def get(self, request):
        all_article = Article.objects.all().order_by('-date_time')[:5]
        flag = 'index'
        return render(request, 'index.html', {
            'all_article': all_article,
            'flag':flag
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


class ArticleListView(View):
    '''
    获取文章列表
    '''
    def get(self, request):
        article_list = Article.objects.all()
        flag = 'list'
        return render(request, 'archives.html',{
            "article_list":article_list,
            "flag":flag
        })


class AboutView(View):
    '''
    取出关于用户信息
    '''
    def get(self, request):
        about = About.objects.all()[0]
        flag = 'about'
        return render(request, 'about.html',{
            "about":about,
            'flag':flag
        })