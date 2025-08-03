from django.db import models
from markdownx.models import MarkdownxField
import uuid
from markdownx.utils import markdownify
from django.utils.html import strip_tags    

# Create your models here.
class Tag(models.Model):
    name=models.CharField('タグ名',max_length=100)
    category=models.ForeignKey('Category',related_name='tag',on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.name

class Miniblog(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title=models.CharField('タイトル',max_length=100)
    summary=models.CharField('要約',max_length=100,null=True,blank=True)
    created_day=models.DateTimeField('作成日時',auto_now_add=True)
    updated_day=models.DateTimeField('更新日時',auto_now=True)
    content=MarkdownxField('内容')
    tag=models.ManyToManyField(Tag,related_name='tag')
    category=models.ForeignKey('Category',related_name='Miniblog',on_delete=models.SET_NULL,null=True,blank=True)
    plain_content = models.TextField(editable=False, blank=True)  
    public=models.BooleanField(verbose_name="公開")

    def save(self, *args, **kwargs):
        html = markdownify(self.content)
        self.plain_content = strip_tags(html)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title
class Category(models.Model):
    name=models.CharField('名前',max_length=100)
    def __str__(self):
        return self.name