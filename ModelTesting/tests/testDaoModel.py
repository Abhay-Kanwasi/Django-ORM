from ModelTesting.models import Services, Category
from django.db import models

class ModelDao:
    """
        - get_enable_categories_with_atleast_one_enabled_service()
        This function will not take any parameters. It will give    you all enable categories with atleast one enable service.

        - disassociate_category_from_service(service, category)
        In this function 2 parameters are needed which will be the instances of the main model. You need to pass them in this function and it will disassociate given category from the given service if both exists.
        
        - get_services_with_enable_categories()
        This function will give you all the services who have active categories in it.

    """
    def get_enable_categories_with_atleast_one_enabled_service():
        categories = Category.objects.filter(is_active=True).filter(services__is_active=True).distinct()
        return categories

    def disassociate_category_from_service(service_object, category_object):
        service_object.categories.remove(category_object)
        return service_object

    def get_services_with_enable_categories():
        services = Services.objects.filter(categories__is_active = True).distinct()
        return services

    # Terminal Input 
    # service1 = Services.objects.get("Service1")
    # update_the_details_of_service(service1)






    