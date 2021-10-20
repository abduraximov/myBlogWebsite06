from django.urls import path
from django.views.generic.edit import CreateView
from .views import ArticleList, ArticleDetail, ArticleUpdate, ArticleDelete, ArticleCreate

urlpatterns = [
    path('', ArticleList.as_view(), name='article_list'),
    path('<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
    path('<int:pk>/edit', ArticleUpdate.as_view(), name='article_edit'),
    path('<int:pk>/delete', ArticleDelete.as_view(), name='article_delete'),
    path('new/', ArticleCreate.as_view(), name='article_create')
]
