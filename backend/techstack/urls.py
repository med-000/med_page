from django.urls import path
from . import views

urlpatterns=[
    path('',views.techstack,name='techstack'),
    path('/main',views.techstack_main,name='techstack_main'),
]