from django.contrib import admin
from .models import Miniblog,Tag,Category
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.
admin.site.register(Miniblog,MarkdownxModelAdmin)
admin.site.register(Tag)
admin.site.register(Category)
