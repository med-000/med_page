from django.shortcuts import render
from .models import Article,Tag,Comment,Category
from django.db.models import Q,Count
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models.functions import TruncDate

# Create your views here.
def home(request):
    articles=Article.objects.all().order_by('created_day')
    articles, selecteds,tags= tagfilter(request,articles)
    return render(request,'blog/home.html',{'articles':articles,'selecteds':selecteds})

@login_required
def home_edit(request):
    return render(request,'blog/home_edit.html')

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
    if request.method == "GET":
        query = request.GET.get('q', '')
        articles = Article.objects.all()

        if query:
            keywords = query.strip().split()
            q_objects = Q()
            for word in keywords:
                q_objects |= Q(plain_content__icontains=word) | Q(title__icontains=word)
            articles = articles.filter(q_objects).distinct()
            
    articles, selecteds,tags= tagfilter(request,articles)
    return render(request,'blog/search.html',{'articles':articles,'tags':tags,'selecteds':selecteds,'query':query})

def category_filter(request,category):
    category=Category.objects.get(name=category)
    articles=Article.objects.filter(category=category)
    articles, selecteds,tags= tagfilter(request,articles)
    return render(request,'blog/category_filter.html',{'category':category,'articles':articles,'selecteds':selecteds})

def tag_filter(request,category,tag):
    category=Category.objects.get(name=category)
    tag=Tag.objects.get(name=tag)
    articles=Article.objects.filter(tag=tag)
    articles, selecteds,tags= tagfilter(request,articles)
    return render(request,'blog/tag_filter.html',{'category':category,'tag':tag,'articles':articles,'selecteds':selecteds})

def archive(request,year,month,day):
    articles = Article.objects.filter(
        created_day__year=year,
        created_day__month=month,
        created_day__day=day
    )
    articles, selecteds,tags= tagfilter(request,articles)
    return render(request,'blog/archive.html',{'articles':articles,'selecteds':selecteds})

def tagfilter(request,articles):
    tags=Tag.objects.all()

    selecteds = request.GET.getlist("tags")
    if selecteds:
        for tag in selecteds:
            articles = articles.filter(tag__name=tag)

    articles = articles.distinct().order_by('-created_day')
    return articles,selecteds,tags


class ArticleCreate(LoginRequiredMixin,generic.CreateView):
    model = Article
    fields = '__all__'
    success_url = '/blog'
    login_url = '/blog'


class ArticleUpdate(LoginRequiredMixin,generic.UpdateView):
    model=Article
    fields='__all__'
    def get_success_url(self):
        return reverse_lazy('article', kwargs={'pk': self.object.id})