from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    
class Services(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    categories = models.ManyToManyField(Category, related_name="services")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name