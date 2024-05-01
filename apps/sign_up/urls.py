from django.urls import path

from apps.sign_up.views import sign_up

urlpatterns=[
    path('', sign_up, name='sign_up')
]