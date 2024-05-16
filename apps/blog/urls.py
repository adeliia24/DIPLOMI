from django.urls import path
from .views import blog, blog_detail, category_blog

urlpatterns=[
    path('', blog, name='blog'),
    path('<int:pk>/', blog_detail, name='blog_detail'),
    path('category_blog/<int:pk>/', category_blog, name='cat_blog'),


]