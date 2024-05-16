from django import  forms

from .models import Comments


class CommentFoodForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=['body']