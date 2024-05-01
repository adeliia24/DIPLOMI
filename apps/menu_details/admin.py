from django.contrib import admin
from apps.menu_details.models import Food,Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
admin.site.register(Category, CategoryAdmin)

class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Food, FoodAdmin)

# Register your models here.
