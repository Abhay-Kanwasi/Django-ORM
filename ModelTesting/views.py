from django.shortcuts import render

from .Dao import ModelDao
from django.http import JsonResponse

def home(request):
    return render(request, "home.html")

def all_forms_along_with_services(request):
    data = ModelDao.get_all_forms_along_with_the_number_of_services_associated()
    return JsonResponse({"data": data})

def all_categories_along_with_the_numbers_of_services_associated(request):
    data = ModelDao.get_all_categories_along_with_the_numbers_of_services_associated()
    return JsonResponse({"data" : data})

def all_services_along_with_the_number_of_categories_associated(request):
    data = ModelDao.get_all_services_along_with_the_number_of_categories_associated()
    return JsonResponse({"data" : data})

def all_services_along_with_the_number_of_form_associated(request):
    data = ModelDao.get_all_services_along_with_the_number_of_form_associated()
    return JsonResponse({"data" : data})