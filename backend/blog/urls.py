from django.urls import path
from . import views
from .views import ArticleCreate,ArticleUpdate
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns=[
    path('',views.home,name='home'),
    path('/login',auth_views.LoginView.as_view(template_name='blog/login.html'),name='login'),
    path('/home_edit',views.home_edit,name='home_edit'),
    path('/category/<str:category>',views.category_filter,name='category_filter'),
    path('/category/<str:category>/tag/<str:tag>',views.tag_filter,name='tag_filter'),
    path('/<int:year>/<int:month>/<int:day>',views.archive,name='archive'), 
    path('/article/<uuid:pk>',views.article,name='article'),
    path('/search',views.search,name='search'),
    path('/article/create',ArticleCreate.as_view(),name='article_create'),
    path('/article/<uuid:pk>/edit',ArticleUpdate.as_view(),name='article_edit'),
]