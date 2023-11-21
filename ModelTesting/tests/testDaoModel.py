from ModelTesting.models import Services, Category
from django.db import models
from django.db.models import Count

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

def get_all_categories_along_with_the_numbers_of_services_associated():
    #  cateories_with_count = Category.objects.annotate(service_count = Count("services"))
    #  print(cateories_with_count.values_list())
    #  for category in cateories_with_count:
    #     print(f"Category : {category.name} | Number of Services : {category.service_count}")
    
    categories = Category.objects.all()
    print(categories.query)
    for category in categories:
        service_count_in_category = category.services.count()
        print(f"Categories {category.name} | Associated Services {service_count_in_category}")



    