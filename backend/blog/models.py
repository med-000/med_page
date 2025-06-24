from django.db import models
from markdownx.models import MarkdownxField
import uuid

# Create your models here.
class Tag(models.Model):
    name=models.CharField('タグ名',max_length=100)
    category=models.ForeignKey('Category',related_name='tag',on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.name

class Article(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title=models.CharField('タイトル',max_length=100)
    summary=models.CharField('要約',max_length=100,null=True,blank=True)
    thumbnail=models.ImageField(upload_to='blog/images/',null=True,blank=True)
    created_day=models.DateTimeField('作成日時',auto_now_add=True)
    updated_day=models.DateTimeField('更新日時',auto_now=True)
    content=MarkdownxField('内容')
    tag=models.ManyToManyField(Tag,related_name='tag')
    category=models.ForeignKey('Category',related_name='article',on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    commentater=models.CharField('コメント者',max_length=100)
    content=models.TextField('コメント')
    day=models.DateTimeField('コメント日時',auto_now_add=True)
    article=models.ForeignKey(Article,on_delete=models.CASCADE,null=True,blank=True,)

class Category(models.Model):
    name=models.CharField('名前',max_length=100)
    def __str__(self):
        return self.name