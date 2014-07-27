from django.contrib import admin
from OneYear.models import Article
from adminsortable.admin import SortableAdminMixin


class ArticleAdmin(SortableAdminMixin, admin.ModelAdmin):
	pass

admin.site.register(Article, ArticleAdmin)