from django.forms import ModelForm
from .models import Reservation


class ReservForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'phone' ]
