from django.shortcuts import render, redirect
from django.urls import  reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from  django.contrib import  messages
from  django.contrib.auth.views import LoginView
from  django.contrib.auth import  authenticate, login, logout
from  django.views import  generic
from django.urls import  reverse_lazy
from .form import  UserCreateForm
from  apps.userProfile.models import Member



class CustomLoginView(LoginView):
    template_name = 'login2.html'

    def get_success_url(self):
        return reverse_lazy('home')

# Create your views here.

def register(request):
    form=UserCreateForm()
    if request.method=='POST':
        form=UserCreateForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            Member.objects.create(user=user, name=username)

            return redirect('login')

    context={
        'form': form
    }
    return render(request, 'sign_up.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password= request.POST.get('password')

        user=authenticate(request, username, password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Пароль или пароль введен не правильно')

    return render(request, 'login2.html')



def logoutPage(request):
    return('login')



