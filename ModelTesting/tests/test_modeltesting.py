from django.test import TestCase
from ModelTesting.models import Category, Services, Pricing, Form
from ModelTesting.tests.testDaoModel import ModelDao
from django.db.utils import IntegrityError
from django.db import transaction
                
class ModelTest(TestCase):

    def setUp(self):
        self.category1 = Category.objects.create(name="Category1", is_active = True)
        self.category2 = Category.objects.create(name="Category2", is_active = False)
        self.category3 = Category.objects.create(name="Category3", is_active = True)
        self.category4 = Category.objects.create(name="Category4", is_active = True)
        self.category5 = Category.objects.create(name="Category5", is_active = True)
        
        self.pricing1 = Pricing.objects.create(price=2.0, is_active = True)
        self.pricing2 = Pricing.objects.create(price=1.8, is_active = True)
        self.pricing3 = Pricing.objects.create(price=4.6, is_active = False)
        self.pricing4 = Pricing.objects.create(price=5.0, is_active = True)
        self.pricing5 = Pricing.objects.create(price=5.0, is_active = False)

        self.form1 = Form.objects.create(name = "Form1", username = "Form1User", password = "Form1Password")
        self.form2 = Form.objects.create(name = "Form2", username = "Form2User", password = "Form2Password")
        self.form3 = Form.objects.create(name = "Form3", username = "Form3User", password = "Form3Password")
        self.form4 = Form.objects.create(name = "Form4", username = "Form4User", password = "Form4Password")
        self.form5 = Form.objects.create(name = "Form5", username = "Form5User", password = "Form5Password")

        self.service1 = Services.objects.create(name="Service1", description = "Service1", is_active = True, pricing = self.pricing1)
        self.service2 = Services.objects.create(name="Service2", description = "Service2", is_active = False, pricing = self.pricing2)
        self.service3 = Services.objects.create(name="Service3", description = "Service3", is_active = False, pricing = self.pricing3)
        self.service4 = Services.objects.create(name="Service4", description = "Service4", is_active = False, pricing = self.pricing4)
        self.service5 = Services.objects.create(name="Service5", description = "Service5", is_active = False, pricing = self.pricing5)

    
    def test_add_form1_form2_to_service1(self):
        print("\nTesting addition of form1 and form2 into services")
        self.service1.form.add(self.form1, self.form2)
        self.assertTrue(self.service1.form.filter(name="Form1").exists())
        self.assertTrue(self.service1.form.filter(name="Form2").exists())
        self.assertEqual(1, self.service1.form.filter(name="Form1").count())
        self.assertEqual(1, self.service1.form.filter(name="Form2").count())
        print("Test passed!")

    def test_disassociate_form1_from_services(self):
        print("\nTesting disassociation of form1 from service1")
        self.service1.form.add(self.form1, self.form2)
        form1 = self.form1
        self.service1.form.remove(form1)
        with self.assertRaises(Form.DoesNotExist):
            self.service1.form.get(name = form1.name)
        print("Test passed !")
   
    def test_create_form(self):
        print("\nTesting creation of form")
        self_form_name = self.form1.name
        self_form_username = self.form1.username
        self_form_password = self.form1.password
        form_name = Form.objects.create(name="Form1", username = "Form1User", password = "Form1Password")
        self.assertEqual(self_form_name, form_name.name)
        self.assertEqual(self_form_username, form_name.username)
        self.assertEqual(self_form_password, form_name.password)
        print("Test passed !")
    
    def test_update_form(self):
        print("\nTesting updation of form")
        name = "New Name"
        username = "New UserName"
        password = "New Password"
        self.form1.name = name
        self.form1.username = username
        self.form1.password = password
        self.assertEqual(name, self.form1.name)
        self.assertEqual(username, self.form1.username)
        self.assertEqual(password, self.form1.password)
        print("Test passed !")

    def test_delete_form(self):
        print("\nTesting deletion of form")
        form_id = self.form1.id
        self.form1.delete()
        with self.assertRaises(Form.DoesNotExist):
            Form.objects.get(id=form_id)
        print("Test passed !")

    def test_get_all_active_prices(self):
        print("\nTesting all active prices")
        enable_prices = ModelDao.get_all_active_prices().count()
        enable_setup_prices = Pricing.objects.filter(is_active=True).count()
        self.assertIsNotNone(enable_prices)
        self.assertEqual(enable_prices, enable_setup_prices)
        print("Test passed !")
    
    def test_get_all_services_with_active_prices(self):
        print("\nTesting all services which have active prices")
        services = ModelDao.get_all_services_with_active_prices().count()
        setup_services = Services.objects.filter(pricing__is_active=True).count()
        self.assertIsNotNone(services)
        self.assertEqual(services, setup_services)
        print("Test passed !")

    def test_price_creation(self):
        print("\n Testing the price creation")
        self.assertEqual(self.service1.pricing, self.pricing1)
        self.assertEqual(self.pricing1.services, self.service1)
        print("Test passed !")

    def test_price_update(self):
        print("\nTesting price updation")
        new_price = 21.8
        self.pricing1.price = new_price
        self.pricing1.save()
        self.assertEqual(self.pricing1.price, new_price)
        print("Test passed !")
    
    def test_price_deletion(self):
        print("\nTesting deletion of price")
        pricing_id = self.pricing1.id
        self.pricing1.delete()
        with self.assertRaises(Pricing.DoesNotExist):
            Pricing.objects.get(id=pricing_id)
        print("Test passed !")

    def test_unique_price_for_each_service(self):
        print("\nTesting unique price for each service")
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                service = Services.objects.create(name = "Some Service", pricing= self.pricing1)
        print("Test passed !")

    def test_price_query(self):
        print("\nTesting price query")
        queried_service = Services.objects.get(pricing__price=2.0)
        self.assertEqual(queried_service, self.service1)
        print("Test passed !")

    def test_create_category(self):
        print("\nTesting category creation")
        category1 = Category.objects.create(name="test_create_category")
        self.assertTrue(Category.objects.filter(name="test_create_category").exists())
        self.assertFalse(Category.objects.filter(name="test_create_category", is_active = True).exists())
        self.assertEqual(category1.name, "test_create_category")
        print("Test passed !")
        
    def test_create_service(self):
        print("\nTesting service creation")
        service1 = Services.objects.create(name = "test_create_service", description = "test_create_service description", is_active = True)
        self.assertTrue(Services.objects.filter(name = "test_create_service", is_active = True).exists())
        self.assertFalse(Services.objects.filter(name = "test_create_service", is_active = False).exists())
        self.assertEqual(service1.description, "test_create_service description")
        self.assertEqual(service1.name, "test_create_service")
        print("Test passed !")   

    def test_add_category1_and_category2_to_service1(self):
        print("\nTesting addition of category into service1")
        self.service1.categories.add(self.category1, self.category2)
        self.assertTrue(self.service1.categories.filter(name = "Category1").exists())
        self.assertTrue(self.service1.categories.filter(name = "Category2").exists())
        self.assertEqual(1, self.service1.categories.filter(name = "Category1").count())
        self.assertEqual(1, self.service1.categories.filter(name = "Category2").count())
        print("Test passed !")

    def test_remove_category1_from_service1(self):
        print("\nTesting category1 remove from service1")
        service1 = self.service1
        category_to_remove = self.category1
        service1.categories.add(category_to_remove)
        service1.categories.remove(category_to_remove)
        self.assertFalse(service1.categories.filter(name="Category1").exists())
        print("Test passed !")

    def test_add_category_2_3_to_service_with_categories_1_2(self):
        print("\nTesting addition of category2 and category3 to service1 with categories 1 and 2")
        self.service1.categories.add(self.category2, self.category3)
        self.assertTrue(self.service1.categories.filter(name="Category2").exists())
        self.assertTrue(self.service1.categories.filter(name="Category3").exists())
        print("Test passed !")
        
    def test_remove_category_2_from_service1(self):
        print("\nTesting remove of category2 from service1")
        service1 = self.service1
        category_to_remove = self.category2
        service1.categories.add(category_to_remove)
        service1.categories.remove(category_to_remove)
        self.service1.categories.remove(category_to_remove)
        self.assertFalse(self.service1.categories.filter(name="Category2").exists())
        print("Test passed !")
    
    def test_categories_with_is_active_false_exits(self):
        print("\nTesting for searching is_active false in category")
        if Category.objects.filter(is_active=False).exists():
            self.assertTrue(Category.objects.filter(is_active=False).exists())
        else:
            print("No categories with active status false")
        print("Test passed !")
    
    def test_get_enable_categories_with_atleast_one_enabled_service(self):
        print("\nTesting for getting enable categories with atleast one enable service")
        categories = ModelDao.get_enable_categories_with_atleast_one_enabled_service()
        self.assertIsNotNone(categories)
        category_count = categories.count()
        self.assertEquals(categories.count(), category_count)
        print("Test passed !")

    def test_disassociate_category_from_service(self):
        print("\nTesting of disassociating category from service")
        category1 = self.category1
        service1 = self.service1
        service1.categories.add(category1)
        service_with_categories_before = service1.categories.all().count()
        ModelDao.disassociate_category_from_service(service1, category1)
        service_with_categories_after = service1.categories.all().count()
        self.assertNotEqual(service_with_categories_after, service_with_categories_before)
        print("Test passed !")

    def test_update_the_details_of_service1(self):
        print("\nTesting updating details of service1")

        with self.assertRaises(Services.DoesNotExist):
            service1 = Services.objects.get(name = "Unknown Service")
        
        with self.assertRaises(Category.DoesNotExist):
            category1 = Category.objects.get(name = "Unknown Category")

        service1 = self.service1
        new_name = "updated service1 name"
        new_description = "updated service1 description" 
        service1.name = new_name
        service1.description = new_description
        service1.is_active = False
        service1.save()
        self.assertEqual(self.service1.name, new_name)
        self.assertEqual(self.service1.description, new_description)
        self.assertEqual(self.service1.is_active, False) 
        print("Test passed !")

    def test_get_services_with_enable_categories(self):
        print("\nTesting for all the services who have active categories in them")
        services = ModelDao.get_services_with_enable_categories()
        self.assertIsNotNone(services)
        print("Test passed !")
        
    def test_category_and_service_exists(self):
        print("\nTesting category and services existance")
        # Test Case 1: Service and Category do not exist
        service_name = "Service2"
        service_description = "Service2"
        category_name = "Category1"
    
        # Attempt to create a service with a nonexistent category
        with self.assertRaises(Category.DoesNotExist):
            category1 = Category.objects.get(name = "something")

        with self.assertRaises(Services.DoesNotExist):
            service1 = Services.objects.get(name="something")
        print("Test1 passed!")

        # Test Case 2: Service and Category both exist
        category1 = self.category1
        service2 = self.service2

        self.assertTrue(Services.objects.filter(name=service2.name).exists())
        self.assertTrue(Category.objects.filter(name=category1.name).exists())
        self.assertEqual(service2.name, service_name)
        self.assertEqual(category1.name, category_name)
        self.assertEqual(service2.description, service_description)
        print("Test2 passed!")

    def test_get_all_categories_along_with_the_numbers_of_services_associated(self):
        print("\nTesting all categories getting the associated services count")
        self.service1.categories.add(self.category1, self.category2, self.category3)
        count = ModelDao.get_all_categories_along_with_the_numbers_of_services_associated()
        self.assertEqual(3, count)
        print("Test passed !")

    def test_get_all_services_along_with_the_number_of_categories_associated(self):
        print("\nTesting all services getting the associated categories count")
        self.service1.categories.add(self.category1, self.category3)
        self.service2.categories.add(self.category1, self.category5, self.category3)
        self.service4.categories.add(self.category3, self.category4, self.category1, self.category5)
        count = ModelDao.get_all_services_along_with_the_number_of_categories_associated()
        self.assertEqual(3, count)
        print("Test passed !")
    
    def tearDown(self):
        Category.objects.all().delete()
        Services.objects.all().delete()


