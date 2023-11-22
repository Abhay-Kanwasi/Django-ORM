from django.contrib import admin
from .models import Category, Services, Pricing, Form, Tasks, Workflow

class TasksAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'task_details']

class WorkflowAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'details']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active']

class PricingAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'is_active']

class FormAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'username', 'password']

class ServicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'is_active']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Pricing, PricingAdmin)
admin.site.register(Form, FormAdmin)