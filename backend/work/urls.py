from django.urls import path
from . import views

urlpatterns=[
    path('',views.work,name='work'),
    path('/<uuid:pk>',views.work_pre,name="work_pre"),
]