from django.db import models
from  django.urls import  reverse
from django.contrib.auth.models import User


# Create your models here.

class Member(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile_image/', default='user.png')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Профиль пользователя '


    def get_absolute_url(self):
        return reverse('post_detail', args=str(self.id))
