from django.contrib import admin
from .models import AboutMe,SocialLink
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.
admin.site.register(AboutMe)
admin.site.register(SocialLink)