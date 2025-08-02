from django.shortcuts import render
from .models import Work,Tag,Category

# Create your views here.
def work(request):
    works=Work.objects.all().order_by('-created_day')
    works=works.filter(public=True)
    return render(request,'work/work_base.html',{'works':works})

def work_pre(request,pk):
    works=Work.objects.get(id=pk)
    return render(request,'work/work_pre.html',{'works':works})
