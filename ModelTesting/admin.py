from django.contrib import admin
from .models import Category, Services


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active']

class ServicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'is_active']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Services, ServicesAdmin)