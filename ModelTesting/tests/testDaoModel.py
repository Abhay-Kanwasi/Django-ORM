from ModelTesting.models import Services, Category, Pricing, Form
from django.db import models
from django.db.models import Count

class ModelDao:
    """
        IN THIS CLASS ALL THE FUNCTIONS FOR TESTING ARE MADE

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

    def disassociate_form_from_service(service_object, form_object):
        service_object.form.remove(form_object)
        return service_object


    def disassociate_form_from_service_by_name(service_name, form_name):
        service_object = Services.objects.get(name=service_name)
        form_object = Form.objects.get(name=form_name)
        service_object.form.remove(form_object)
        return service_object


    def disassociate_form_from_service_by_id(service_id, form_id):
        service_object = Services.objects.get(id=service_id)
        form_object = Form.objects.get(name=form_id)
        service_object.form.remove(form_object)
        return service_object

    def get_services_with_enable_categories():
        services = Services.objects.filter(categories__is_active = True).distinct()
        return services 

    def get_all_forms_along_with_the_number_of_services_associated():
        forms = Form.objects.all()
        list_of_forms = []
        for form in forms:
            form_dict = dict()
            form_dict["name"] = form.name
            form_dict["username"] = form.username
            form_dict["password"] = form.password
            form_dict["services_count"] = form.services.count()
            list_of_forms.append(form_dict)
        return list_of_forms

    def get_all_categories_along_with_the_numbers_of_services_associated():
        categories = Category.objects.all()
        list_of_categories = []
        for category in categories:
            category_dict = dict()
            category_dict["name"] = category.name
            category_dict["is_active"] = category.is_active
            category_dict["services_count"] = category.services.count()
            list_of_categories.append(category_dict)
        return list_of_categories

    def get_all_services_along_with_the_number_of_form_associated():
        """
        @Returns a list containing service details and the number of forms associated with the service
        For example:
        [
            {"name": "service name1": "description": "Service name1 description", "is_active": True, "CountForms": 10  },
            {"name": "service name2": "description": "Service name2 description", "is_active": True, "CountForms": 0  },
        ]
        """
        services = Services.objects.all()
        list_of_services = []
        for service in services:
            services_dict = dict()
            services_dict["name"] = service.name
            services_dict["description"] = service.description
            services_dict["is_active"] = service.is_active
            services_dict["form_count"] = service.form.count()
            list_of_services.append(services_dict)
        return list_of_services        

    def get_all_services_along_with_the_number_of_categories_associated():
        services = Services.objects.all()
        list_of_services = []
        for service in services:
            services_dict = dict()
            services_dict["name"] = service.name
            services_dict["description"] = service.description
            services_dict["is_active"] = service.is_active
            services_dict["category_count"] = service.categories.count()
            list_of_services.append(services_dict)
        return list_of_services