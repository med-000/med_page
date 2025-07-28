from django.urls import path
from . import views

urlpatterns=[
    path('',views.techstack,name='techstack'),
]