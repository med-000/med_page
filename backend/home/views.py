from django.shortcuts import render
from .models import SocialLink,AboutMe
# Create your views here.
def home(request):
    SocialLinks = SocialLink.objects.all()
    aboutme=AboutMe.objects.first()
    return render(request,'home/home_base.html',{'SocialLinks':SocialLinks,'aboutme':aboutme})

def aboutme(request):
    SocialLinks = SocialLink.objects.all()
    aboutme=AboutMe.objects.first()
    return render(request,'home/about_me.html',{'SocialLinks':SocialLinks,'aboutme':aboutme})
