from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from apps.menu_details.models import Category, Food


# Create your views here.
def menu(request):
    category = Category.objects.all()
    foods = Food.objects.order_by('?')
    paginator = Paginator(foods, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'category': category,
        'foods': page_obj
    }
    return render(request, 'menu.html', context)


def category_menu(request, pk):

    foods = get_object_or_404(Food, id=pk)
    context = {
        'foods': foods
    }
    return redirect(request, 'cat_menu.html', context)
