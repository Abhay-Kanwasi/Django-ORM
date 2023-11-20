from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def get_enable_categories_with_atleast_one_enabled_service(self):
        active_categories = Category.objects.filter(
            is_active=True,
            services__is_active=True
        ).distinct()
        return active_categories
    
    
class Services(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    categories = models.ManyToManyField(Category, related_name="services")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name