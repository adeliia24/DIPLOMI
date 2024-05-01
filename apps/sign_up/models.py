from django.db import models

# Create your models here.
class Users(models.Model):
    username=models.CharField(max_length=100)
    e_mail=models.EmailField()
    password=models.CharField(max_length=8)
    address=models.CharField(max_length=100, blank=True)
    phone=models.CharField(max_length=100, blank=True)
    avatar=models.ImageField(upload_to='avatars/', blank=True)

    class Meta:
        verbose_name_plural='Пользователи'

    def __str__(self):
        return self.username