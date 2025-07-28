from django.shortcuts import render

# Create your views here.
def miniblog(request):
    return render(request,'miniblog/miniblog_base.html')