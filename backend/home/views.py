from django.shortcuts import render
from .models import SocialLink,AboutMe
from collections import defaultdict
from django.db.models.functions import ExtractYear
from history.models import History
# Create your views here.
from django.shortcuts import render
from .models import SocialLink, AboutMe
from collections import defaultdict
from django.db.models.functions import ExtractYear
from history.models import History

def home(request):
    SocialLinks = SocialLink.objects.all()
    aboutme = AboutMe.objects.first()

    histories = History.objects.annotate(year=ExtractYear('start_day')).order_by('-year', '-start_day')
    group_histories = defaultdict(list)
    for h in histories:
        group_histories[h.year].append(h)

    return render(request, 'home/home_base.html', {
        'SocialLinks': SocialLinks,
        'aboutme': aboutme,
        'group_histories': dict(group_histories), 
    })


def aboutme(request):
    SocialLinks = SocialLink.objects.all()
    aboutme=AboutMe.objects.first()
    return render(request,'home/about_me.html',{'SocialLinks':SocialLinks,'aboutme':aboutme})

def profile(request):
    SocialLinks = SocialLink.objects.all()
    aboutme=AboutMe.objects.first()
    return render(request,'home/profile.html',{'SocialLinks':SocialLinks,'aboutme':aboutme})