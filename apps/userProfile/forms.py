from .models import Member
from django import  forms


class MemberForm(forms.ModelForm):
    class Meta:
        model=Member
        fields=['name', 'email', 'phone', 'address']