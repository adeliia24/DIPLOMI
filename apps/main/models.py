from django.db import models

# Create your models here.
class Reservation(models.Model):
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    status=models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Бронирование столика'