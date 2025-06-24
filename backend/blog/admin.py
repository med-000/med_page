from django.contrib import admin
from .models import Article,Tag,Comment,Category
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.
admin.site.register(Article,MarkdownxModelAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Category)