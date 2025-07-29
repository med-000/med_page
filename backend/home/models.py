from django.db import models

# Create your models here.
class AboutMe(models.Model):
    name=models.CharField('名前',max_length=50)
    headerimage=models.ImageField(upload_to='home/images/',null=True,blank=True)
    iconimage=models.ImageField(upload_to='home/images/',null=True,blank=True)
    aboutme=models.TextField('about=me',null=True,blank=True)
    def __str__(self):
        return self.name
    
class SocialLink(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='home/images/',null=True,blank=True)
    def __str__(self):
        return self.name