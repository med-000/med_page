from django.shortcuts import render
import requests
from django.conf import settings
from .models import TechStack,Category
# Create your views here.
def techstack(request):
    techstacks=TechStack.objects.all()
    categories=Category.objects.all()

    return render(request, 'techstack/techstack_base.html', {
        'techstacks': techstacks,
        'categories':categories,
    })

def techstack_main(request):
    techstacks=TechStack.objects.all()

    url = settings.WAKATIME_API_URL

    response = requests.get(url)

    categories=Category.objects.all()

    if response.status_code == 200:

        json_data = response.json()

        langs = json_data["data"]["languages"]
        dependencies=json_data["data"]["dependencies"]


        language_category,_=Category.objects.get_or_create(name="Language")
        dependencies_category,_=Category.objects.get_or_create(name="Library")


        for lang in langs:
            try:
                obj = TechStack.objects.get(name=lang["name"])
                obj.percent = lang["percent"]
                obj.time = lang["total_seconds"]
                obj.category = language_category
                obj.save()
            except TechStack.DoesNotExist:
                TechStack.objects.create(
                    name=lang["name"],
                    content="編集中",
                    percent=lang["percent"],
                    time=lang["total_seconds"],
                    category=language_category,
                    public=True 
                )


        for dependence in dependencies:
            try:
                obj = TechStack.objects.get(name=dependence["name"])
                obj.percent = dependence["percent"]
                obj.time = dependence["total_seconds"]
                obj.category = dependencies_category
                obj.save()
            except TechStack.DoesNotExist:
                TechStack.objects.create(
                    name=dependence["name"],
                    content="編集中",
                    percent=dependence["percent"],
                    time=dependence["total_seconds"],
                    category=dependencies_category,
                    public=True
                )


        techstacks=techstacks.filter(public=True)

        return render(request, 'techstack/techstack_main.html', {
            'techstacks': techstacks,
            'categories':categories,
        })

    else:
        return render(request, 'techstack/techstack_main.html', {
            'techstacks': "取得失敗",
            'categories':categories,
        })