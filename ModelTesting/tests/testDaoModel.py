from ModelTesting.models import Services, Category, Pricing
from django.db import models
from django.db.models import Count

class ModelDao:
    """
        - get_enable_categories_with_atleast_one_enabled_service()
        This function will not take any parameters. It will give    you all enable categories with atleast one enable service.

        - disassociate_category_from_service(service, category)
        In this function, 2 parameters are needed which will be the instances of the main model. You need to pass them in this function and it will disassociate given category from the given service if both exists.
        
        - get_services_with_enable_categories()
        This function will give you all the services who have active categories in it.

        - get_all_categories_along_with_the_numbers_of_services_associated()
        This function will get all categories along with all the services count that are associated with category.

        # Another method can be used
        cateories_with_count = Category.objects.annotate(service_count = Count("services"))
        print(cateories_with_count.values_list())
        for category in cateories_with_count:
        print(f"Category : {category.name} | Number of Services : {category.service_count}")

        - get_all_services_along_with_the_number_of_categories_associated() 
        This function will get all the services along with all the categories count that are associated with service.

    """

    def get_all_services_with_active_prices():
        services_with_active_price = Services.objects.filter(pricing__is_active=True)
        return services_with_active_price

    def get_all_active_prices():
        enable_prices = Pricing.objects.filter(is_active=True)
        return enable_prices

    def get_enable_categories_with_atleast_one_enabled_service():
        enable_categories = Category.objects.filter(is_active=True).filter(services__is_active=True).distinct()
        return enable_categories

    def disassociate_category_from_service(service_object, category_object):
        service_object.categories.remove(category_object)
        return service_object

    def get_services_with_enable_categories():
        services = Services.objects.filter(categories__is_active = True).distinct()
        return services 

    def get_all_categories_along_with_the_numbers_of_services_associated():
        categories = Category.objects.all()
        count = 0
        for category in categories:
            service_count_in_categories = category.services.count()
            print(f"Categories {category.name} | Associated Services {service_count_in_categories}")
            if service_count_in_categories != 0:
                count += 1
        return count

    def get_all_services_along_with_the_number_of_categories_associated():
        services = Services.objects.all()
        count = 0
        for service in services:
            category_count_in_services = service.categories.count()
            print(f"Service {service.name} | Associated Categories {category_count_in_services}")
            if category_count_in_services != 0:
                count += 1
        return count