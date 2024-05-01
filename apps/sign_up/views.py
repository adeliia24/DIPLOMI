from django.shortcuts import render, redirect

from apps.sign_up.forms import RegisterUserForm

# Create your views here.
def sign_up(request):
    if request.method== 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
          
            user.save()
            message='Вы прошли регистрацию'
            return render(request, 'sign_up.html',{'message':message})
        else:
            message='Пароль не совпадает'
            return render(request, 'sign_up.html',{'message':message})
    else:
        form = RegisterUserForm()

    return render(request, 'sign_up.html')










