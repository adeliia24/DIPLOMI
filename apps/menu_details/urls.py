from django.urls import  path

from apps.menu_details.views import menu_details

urlpatterns=[
    path('menu_details/<str:slug>', menu_details, name='menu_details')
]

