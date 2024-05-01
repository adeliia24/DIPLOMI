from django.urls import path
from .views import register, CustomLoginView, loginPage, logoutPage


urlpatterns=[

    path('register/', register, name='register'),
    path('', CustomLoginView.as_view(), name='login'),
    path('', loginPage, name='login'),
    path('register/logout', logoutPage, name='logout')



]