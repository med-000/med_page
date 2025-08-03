from django.urls import path
from . import views

urlpatterns=[
    path('',views.miniblog,name='miniblog'),
    path('/<uuid:pk>',views.miniblog_pre,name='miniblog_pre')
]