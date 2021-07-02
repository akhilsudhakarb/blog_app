from django.urls import path
from . import views
from .views import ArticleDetailView, AddArticleView, UpdateArticleView, DeleteArticleView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<str:cats>', views.blog_by_cat, name='category'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add-article/', AddArticleView.as_view(), name='add-article'),
    path('update-article/<int:pk>', UpdateArticleView.as_view(), name='update-article'),
    path('delete-article/<int:pk>', DeleteArticleView.as_view(), name='delete-article'),

]
