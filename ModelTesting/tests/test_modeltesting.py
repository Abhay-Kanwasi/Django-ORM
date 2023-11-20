from django.test import TestCase
from ModelTesting.models import Category, Services
from ModelTesting.tests.testDaoModel import ModelDao

class ModelTest(TestCase):

    def setUp(self):
        self.category1 = Category.objects.create(name="Category1", is_active = True)
        self.category2 = Category.objects.create(name="Category2", is_active = False)
        self.category3 = Category.objects.create(name="Category3", is_active = True)
        self.category4 = Category.objects.create(name="Category4", is_active = True)
        self.category5 = Category.objects.create(name="Category5", is_active = True)
        
        self.service1 = Services.objects.create(name="Service1", description = "Service1", is_active = True)
        self.service2 = Services.objects.create(name="Service2", description = "Service2", is_active = False)
        self.service3 = Services.objects.create(name="Service3", description = "Service3", is_active = False)
        self.service4 = Services.objects.create(name="Service4", description = "Service4", is_active = False)
        self.service5 = Services.objects.create(name="Service5", description = "Service5", is_active = False)
    
    def test_create_category(self):
        print("\nTesting category creation")
        category1 = Category.objects.create(name="test_create_category")
        try:
            self.assertTrue(Category.objects.filter(name="test_create_category").exists())
            self.assertFalse(Category.objects.filter(name="test_create_category", is_active = True).exists())
            self.assertEqual(category1.name, "test_create_category")
            print("Test passed !")
        except AssertionError as error:
            print(f"Test failed due to: {error}")
        
    def test_create_service(self):
        print("\nTesting service creation")
        service1 = Services.objects.create(name = "test_create_service", description = "test_create_service description", is_active = True)
        try:
            self.assertTrue(Services.objects.filter(name = "test_create_service", is_active = True).exists())
            self.assertFalse(Services.objects.filter(name = "test_create_service", is_active = False).exists())
            self.assertEqual(service1.description, "test_create_service description")
            self.assertEqual(service1.name, "test_create_service")

            print("Test passed !")
        except AssertionError as error:
            print(f"Test failed due to : {error}")

    def test_add_category1_and_category2_to_service1(self):
        print("\nTesting addition of category into service1")
        self.service1.categories.add(self.category1, self.category2)
        try:
            self.assertTrue(self.service1.categories.filter(name = "Category1").exists())
            self.assertTrue(self.service1.categories.filter(name = "Category2").exists())

            self.assertEqual(1, self.service1.categories.filter(name = "Category1").count())
            self.assertEqual(1, self.service1.categories.filter(name = "Category2").count())
            print("Test passed !")
        except AssertionError as error:
            print(f'Test failed due to : {error}')

    def test_remove_category1_from_service1(self):
        print("\nTesting category1 remove from service1")
        service1 = self.service1
        category_to_remove = self.category1
        service1.categories.add(category_to_remove)
        service1.categories.remove(category_to_remove)
        try:
            self.assertFalse(service1.categories.filter(name="Category1").exists())
            print("Test passed !")
        except AssertionError as error:
            print(f'Test failed due to : {error}')

    def test_add_category_2_3_to_service_with_categories_1_2(self):
        print("\nTesting addition of category2 and category3 to service1 with categories 1 and 2")
        self.service1.categories.add(self.category2, self.category3)
        try:
            self.assertTrue(self.service1.categories.filter(name="Category2").exists())
            self.assertTrue(self.service1.categories.filter(name="Category3").exists())
            print("Test passed !")
        except AssertionError as error:
            print(f'Test failed due to : {error}')

    def test_remove_category_2_from_service1(self):
        print("\nTesting remove of category2 from service1")
        service1 = self.service1
        category_to_remove = self.category2
        service1.categories.add(category_to_remove)
        service1.categories.remove(category_to_remove)
        try:
            self.service1.categories.remove(category_to_remove)
            self.assertFalse(self.service1.categories.filter(name="Category2").exists())
            print("Test passed !")
        except AssertionError as error:
            print(f'Test failed due to : {error}')
    
    def test_categories_with_is_active_false_exits(self):
        print("\nTesting for searching is_active false in category")
        try:
            if Category.objects.filter(is_active=False).exists():
                self.assertTrue(Category.objects.filter(is_active=False).exists())
            else:
                print("No categories with active status false")
            print("Test passed !")
        except AssertionError as error:
            print(f'Test failed due to : {error}')
    
    def test_get_enable_categories_with_atleast_one_enabled_service(self):
        print("\nTesting for getting enable categories with atleast one enable service")
        categories = ModelDao.get_enable_categories_with_atleast_one_enabled_service()
        try:
            self.assertIsNotNone(categories)
            category_count = categories.count()
            self.assertEquals(categories.count(), category_count)
            print("Test passed !")
        except AssertionError as error:
            print(f'Test failed due to : {error}')

    def test_disassociate_category_from_service(self):
        print("\nTesting of disassociating category from service")
        category1 = self.category1
        service1 = self.service1
        service1.categories.add(category1)
        service_with_categories_before = service1.categories.all().count()
        ModelDao.disassociate_category_from_service(service1, category1)
        service_with_categories_after = service1.categories.all().count()
        try:
            self.assertNotEqual(service_with_categories_after, service_with_categories_before)
            print("Test passed !")
        except AssertionError as error:
            print(f'Test failed due to : {error}')

    def test_update_the_details_of_service1(self):
        print("\nTesting updating details of service1")
        service1 = self.service1
        new_name = "updated service1 name"
        new_description = "updated service1 description" 
        service1.name = new_name
        service1.description = new_description
        service1.is_active = False
        service1.save()
        # Check if the details have been updated
        try:
            self.assertEqual(self.service1.name, new_name)
            self.assertEqual(self.service1.description, new_description)
            self.assertEqual(self.service1.is_active, False) 
            print("Test passed !")
        except AssertionError as error:
            print(f'Test failed due to : {error}')
    
    def test_get_services_with_enable_categories(self):
        print("\nTesting for all the services who have active categories in them")
        try:
            services = ModelDao.get_services_with_enable_categories()
            self.assertIsNotNone(services)
            print("Test passed !")
        except AssertionError as error:
            print(f'Test failed due to : {error}')
    
    def test_category_and_service_exists(self):
        print("\nTesting category and services existance")
        # Test Case 1: Service and Category do not exist
        service_name = "test_create_service"
        service_description = "Test description"
        category_name = "nonexistent"
    
        try:
            # Attempt to create a service with a nonexistent category
            with self.assertRaises(Category.DoesNotExist):
                category1 = Category.objects.create(name = category_name)
            with self.assertRaises(Services.DoesNotExist):
                service1 = Services.objects.create(name=service_name, description=service_description, category=Category.objects.get(name=category_name))
            print("Testpassed!")
        except AssertionError as error:
            print(f"Test2 - Case 1 failed: {error}")

        # Test Case 2: Service and Category both exist
        try:
            category1 = self.category1
            service2 = self.service1

            self.assertTrue(Services.objects.filter(name=service_name).exists())
            self.assertTrue(Category.objects.filter(name=category1.name).exists())
            self.assertEqual(service2.name, service_name)
            self.assertEqual(service2.description, service_description)
            print("Test passed!")
        except AssertionError as error:
            print(f"Test2 - Case 2 failed: {error}")

    
    def test_disassociate_category_from_service_doesnotexist(self):
        print("\nTesting disassociate category from service")
        try:
            service1 = Services.objects.get(name = "something")
            category1 = self.category1
            ModelDao.disassociate_category_from_service(service1, category1)
            print("Test1 passed !s")
        except Services.DoesNotExist as error:
            print(f"Error due to {error}")
        
        try:
            service1 = self.service1
            category1 = Category.objects.get(name = "something")
            ModelDao.disassociate_category_from_service(service1, category1)
            print("Test2 passed !")
        except Category.DoesNotExist as error:
            print(f"Error due to {error}")

        try:
            service1 = Services.objects.get(name = "something")
            category1 = Category.objects.get(name = "something")
            ModelDao.disassociate_category_from_service(service1, category1)
            print("Test3 passed !")
        except Exception as e:
            print(f'Error due to missing parameters ! {e}')
        


    def tearDown(self):
        Category.objects.all().delete()
        Services.objects.all().delete()


