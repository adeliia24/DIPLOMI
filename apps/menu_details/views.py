from django.shortcuts import render, get_object_or_404
from  apps.menu_details.models import Food
from .forms import CommentFoodForm
from .models import Comments

# Create your views here.
def menu_details(request, slug):
    foods=get_object_or_404(Food, slug=slug)
    comments=Comments.objects.filter(food=foods)
    if request.method=='POST':
        form=CommentFoodForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.user=request.user
            comment.food=foods
            comment.save()
    else:
        form=CommentFoodForm()
    context={
        'foods': foods,
        'form': form,

            }
    return render(request, 'menu_details.html', context)