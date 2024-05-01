from django import forms

from apps.sign_up.models import Users


class RegisterUserForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Users
        fields = ['username', 'e_mail', 'password']

