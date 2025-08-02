from collections import defaultdict
from django.db.models.functions import ExtractYear
from django.shortcuts import render
from .models import History,Tag,Category

# Create your views here.
def history(request):
    histories=History.objects.annotate(year=ExtractYear('start_day')).order_by('-year','-start_day')

    group_histories=defaultdict(list)

    for h in histories:
        group_histories[h.year].append(h)

    return render(request,'history/history_base.html',{'histories':histories,'group_histories':dict(group_histories)})