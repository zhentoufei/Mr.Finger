"""mrfinger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic import TemplateView

from articles.views import ArticleView, ArticleDetailView, ArticleListView, AboutView
from mrfinger.settings import STATIC_ROOT, MEDIA_ROOT
import xadmin
from django.views.static import serve

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$',ArticleView.as_view(), name="index"),
    url(r'^archives/',ArticleListView.as_view(), name="archives"),
    url(r'^detail/(?P<article_id>\d+)/$',ArticleDetailView.as_view(), name="detail"),
    url(r'^about/',AboutView.as_view(), name="about"),
    url('^rss/', AboutView.as_view(), name="rss"),
    # url('^rss/', AboutView.as_view(), name="rss"),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
]


handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_not_found'
