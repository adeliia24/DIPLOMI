from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import MemberForm

from .models import Member


# Create your views here.
def profile(request):
    profile = get_object_or_404(Member, user=request.user)
    context = {
        'profile': profile
    }
    return render(request, 'profile.html', context)


def editprofile(request):
    profile = get_object_or_404(Member, user=request.user)

    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Подставьте имя вашего URL-шаблона для перенаправления после успешного сохранения
    else:
        form = MemberForm(instance=profile)

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'editprofile.html', context)


class EditProfileView(generic.UpdateView):
    model = Member
    template_name = 'editProfile.html'
    fields = ['name', 'email', 'phone', 'address']
    success_url = reverse_lazy('profile')


    def get_object(self, queryset=None):
        # Получаем объект Member для текущего пользователя
        return get_object_or_404(Member, user=self.request.user)

    def form_valid(self, form):
        # Сохраняем изменения
        self.object = form.save()
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем объект Member для текущего пользователя
        profile = get_object_or_404(Member, user=self.request.user)
        context['profile'] = profile
        return context

