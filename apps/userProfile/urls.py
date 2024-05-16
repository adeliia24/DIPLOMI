from django.urls import  path
from .views import profile,editprofile, EditProfileView

urlpatterns =[
    path('', profile, name='profile'),
    path('edit_profile/', editprofile, name='editprofile'),

]