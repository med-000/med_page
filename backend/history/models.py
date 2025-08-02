from django.db import models
import uuid

# Create your models here.
class Tag(models.Model):
    name=models.CharField('タグ名',max_length=100)
    category=models.ForeignKey('Category',related_name='tag',on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.name
    
class History(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField('タイトル',max_length=100)
    content=models.TextField('内容',max_length=500)
    start_day=models.DateTimeField('開始日時')
    end_day=models.DateTimeField('終了日時',null=True,blank=True)
    tag=models.ManyToManyField(Tag,related_name='tag')
    category=models.ForeignKey('Category',related_name='history',on_delete=models.SET_NULL,null=True,blank=True)
    public=models.BooleanField(verbose_name="公開")
    url=models.URLField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name=models.CharField('名前',max_length=100)
    def __str__(self):
        return self.name