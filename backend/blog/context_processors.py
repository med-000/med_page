from .models import Article,Tag,Comment,Category
from django.db.models import Count
from django.db.models.functions import TruncDate
from .views import tagfilter


def sidebar_context(request):
    tags=Tag.objects.all()
    categories=Category.objects.all()
    archive_dates = (
        Article.objects
        .annotate(date=TruncDate('created_day'))
        .values('date')
        .annotate(count=Count('id'))
        .order_by('-date')
    )
    return {'sidebar_tags':tags,'sidebar_categories':categories,'sidebar_archive_dates':archive_dates}

def mainbar_context(request):
    tags, articles, selecteds= tagfilter(request)
    return{'mainbar_tags':tags,'mainbar_articles':articles,'mainbar_selecteds':selecteds}