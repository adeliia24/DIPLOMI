from django.urls import  path

from apps.menu.views import menu, category_menu

urlpatterns=[
    path('', menu, name='menu'),
    path('category_menu/<int:pk>/', category_menu, name='categorymenu')
]

