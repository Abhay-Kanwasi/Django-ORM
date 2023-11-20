from ModelTesting.models import Services, Category
from django.db import models

def get_enable_categories_with_atleast_one_enabled_service():
    """
        c1e s1e, s2d, s3e Selected
        c2d s1e, s2d, s3e Not Selected
        c3e s1d, s2d, s3d Not Selected
        c4e Not Selected
        c5e s1d, s2d, s3e Selected
    """
    # Please add related_name = "services" in for this to work
    categories = Category.objects.filter(is_active=True).filter(services__is_active=True).distinct()
    return categories

def disassociate_category_from_service(service_name, category_name):
    category = Category.objects.get(name=category_name)
    service = Services.objects.get(name=service_name)
    service.categories.remove(category)


def update_the_details_of_service(service):
    service.save()

    # Terminal Input 

    # service1 = Services.objects.get("Service1")
    # update_the_details_of_service(service1)





    