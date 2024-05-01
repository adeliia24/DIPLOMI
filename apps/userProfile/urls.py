from django.urls import  path
from .views import profile,editProfile, EditProfileView

urlpatterns =[
    path('', profile, name='profile'),
    path('edit_profile/', editProfile, name='editProfile'),

]