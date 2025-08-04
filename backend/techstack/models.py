from django.db import models

# Create your models here.
class TechStack(models.Model):
    name=models.CharField('名前',max_length=100)
    content=models.TextField('一言',max_length=500)
    percent=models.FloatField()
    time=models.FloatField()
    image=models.ImageField(upload_to='techstack/images/',null=True,blank=True)
    category=models.ForeignKey('Category',related_name='work',on_delete=models.SET_NULL,null=True,blank=True)
    public=models.BooleanField(verbose_name="公開")
    @property
    def display_time(self):
        seconds = int(self.time)
        if seconds >= 3600:
            return f"{seconds // 3600}h {((seconds % 3600) // 60)}m"
        elif seconds >= 60:
            return f"{seconds // 60}m"
        else:
            return f"{seconds}s"
    def __str__(self):
        return self.name
class Category(models.Model):
    name=models.CharField('名前',max_length=100)
    def __str__(self):
        return self.name