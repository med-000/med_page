from django.shortcuts import render
from .models import Article,Tag,Comment
from django.db.models import Q

# Create your views here.
def home(request):
    articles=Article.objects.all().order_by('created_day')
    tags, articles, selecteds= tagfilter(request)
    return render(request,'blog/home.html',{'articles':articles,'tags':tags,'selecteds':selecteds})

def article(request,pk):
    article=Article.objects.get(id=pk)
    comments=Comment.objects.filter(article=article)
    articles = Article.objects.filter(tag__name__in=article.tag.values_list('name', flat=True)).exclude(id=pk).order_by('created_day')
    if request.method == 'POST':
        commentater=request.POST['author']
        content=request.POST['comment']

        comment=Comment.objects.create(commentater=commentater, content=content, article=article)
        comment.save()
    return render(request,'blog/article.html',{'article':article,'comments':comments,'articles':articles})

def search(request):
    tags=Tag.objects.all()
    text_search=""
    searched=False
    if request.method == "GET":
        text_search=request.GET.get("q","")
        text_search = text_search.strip()
        keywords = text_search.split()
        query = Q()
        for word in keywords:
            query &= (Q(summary__icontains=word) | Q(title__icontains=word))

        searched = bool(text_search)

        if searched:
            articles = Article.objects.filter(query).distinct().order_by('created_day')
        else:
            articles = Article.objects.none()
    return render(request,'blog/search.html',{'articles':articles,'tags':tags,'text_search':text_search,'searched':searched})

def tagfilter(request):
    tags=Tag.objects.all()
    articles=Article.objects.all().order_by('created_day')
    
    selecteds = request.GET.getlist("tags")
    if selecteds:
        articles = Article.objects.all()
    for tag in selecteds:
        articles = articles.filter(tag__name=tag)

    articles = articles.distinct().order_by('created_day')
    return tags, articles,selecteds