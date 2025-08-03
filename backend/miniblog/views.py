from django.shortcuts import render
from .models import Miniblog,Tag,Category

# Create your views here.
def miniblog(request):
    miniblogs=Miniblog.objects.all().order_by('-created_day')
    miniblogs=miniblogs.filter(public=True)
    return render(request,'miniblog/miniblog_base.html',{"miniblogs":miniblogs})

def miniblog_pre(request,pk):
    miniblog=Miniblog.objects.get(id=pk)
    return render(request,'miniblog/miniblog_pre.html',{"miniblog":miniblog})