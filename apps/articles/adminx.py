from .models import Article, Tag
import xadmin


class ArticleAdmin(object):
    list_display = ['title', 'category', 'tag', 'date_time', 'content']
    style_fields = {"content":"ueditor"}


class TagAdmin(object):
    list_display = ['tag_name']


xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Tag, TagAdmin)
