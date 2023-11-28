from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('api1/', views.all_forms_along_with_services, name="api1"),
    path('api2/', views.all_categories_along_with_the_numbers_of_services_associated, name="api2"),
    path('api3/', views.all_services_along_with_the_number_of_categories_associated, name="api3"),
    path('api4/', views.all_services_along_with_the_number_of_form_associated, name="api4"),
]
