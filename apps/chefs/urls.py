from django.urls import  path
from .views import chefs


urlpatterns=[
    path('', chefs, name='chefs')
]