from django.shortcuts import render, redirect
from .forms import ReservForm
from apps.chefs.models import Chefs
from apps.blog.models import News
from  apps.menu_details.models import Category



# Create your views here.
def main(request):
    chefs= Chefs.objects.all()
    news=News.objects.all()[:4]
    category=Category.objects.all()


    if request.method == 'POST':
        form = ReservForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReservForm()

    context = {
        'form': form,
        'chefs': chefs,
        'news': news,
        'category':category


    }
    return render(request, 'index.html', context)



