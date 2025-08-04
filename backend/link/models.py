from django.db import models

# Create your models here.
class Link(models.Model):
    name=models.CharField('名前',max_length=100)
    image=models.ImageField(upload_to='link/images/',null=True,blank=True)
    category=models.ForeignKey('Category',related_name='link',on_delete=models.SET_NULL,null=True,blank=True)
    public=models.BooleanField(verbose_name="公開")
    url=models.URLField(max_length=200)

    def __str__(self):
        return self.name
class Category(models.Model):
    name=models.CharField('名前',max_length=100)
    def __str__(self):
        return self.name