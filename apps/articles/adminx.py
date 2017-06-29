from .models import Article, Tag, About
import xadmin


class ArticleAdmin(object):
    list_display = ['title', 'category', 'tag', 'date_time', 'content']
    style_fields = {"content":"ueditor"}


class TagAdmin(object):
    list_display = ['tag_name']

class AboutAdmin(object):
    list_display = ['about', 'date_time']
    style_fields = {"about": "ueditor"}


xadmin.site.register(About, AboutAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Article, ArticleAdmin)
