from django.shortcuts import render

# Create your views here.
def techstack(request):
    return render(request,'techstack/techstack_base.html')