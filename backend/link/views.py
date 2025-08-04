from django.shortcuts import render
from .models import Link,Category
# Create your views here.
def link(request):
    links=Link.objects.all()
    categories=Category.objects.all()
    links=links.filter(public=True)
    return render(request,'link/link_base.html',{'links':links,'categories':categories})