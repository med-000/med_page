from django.shortcuts import render

# Create your views here.
def link(request):
    return render(request,'link/link_base.html')