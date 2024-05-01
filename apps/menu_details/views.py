from django.shortcuts import render, get_object_or_404
from  apps.menu_details.models import Food

# Create your views here.
def menu_details(request, slug):
    foods=get_object_or_404(Food, slug=slug)
    context={
        'foods': foods
    }
    return render(request, 'menu_details.html', context)