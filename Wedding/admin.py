from django.contrib import admin
from Wedding.models import Article
from adminsortable.admin import SortableAdmin


class ArticleAdmin(SortableAdmin, admin.ModelAdmin):
	pass

admin.site.register(Article, ArticleAdmin)