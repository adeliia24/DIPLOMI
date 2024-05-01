from django.db import models
from django.urls import  reverse
class Category(models.Model):
    name=models.CharField("название", max_length=50)
    slug=models.SlugField(max_length=100)

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name_plural='Категория блюд'
class Food(models.Model):
    name=models.CharField('Имя продукта', max_length=50, unique=True)
    price= models.IntegerField('Цена', default=0)
    price_medium=models.IntegerField('Цена для медиум',default=0)
    price_small=models.IntegerField('Цена для маленькой',default=0)
    briefly=models.CharField("Коротко о еде", max_length=200)
    image=models.ImageField(upload_to='menu/')
    slug=models.SlugField(unique=True, max_length=100)
    description=models.TextField('Все о еде')
    discount=models.IntegerField('Скидки', default=0, blank=True)
    discount_main=models.BooleanField(default=False)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Блюдо'


    def get_absolute_url(self):
        return reverse('menu_details', kwargs={'slug': self.slug})
