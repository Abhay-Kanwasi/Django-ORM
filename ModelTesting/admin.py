from django.contrib import admin
from .models import Category, Services, Pricing


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active']

class PricingAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'is_active']

class ServicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'is_active']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Pricing, PricingAdmin)