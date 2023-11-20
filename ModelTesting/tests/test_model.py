from django.test import TestCase
from ModelTesting.ServiceDao import get_enable_categories_with_atleast_one_enabled_service, disassociate_category_from_service, update_the_details_of_service
from ModelTesting.models import Category, Services


class ModelTest(TestCase):
    """
       s1e s2d se3 s4d s5d
       c1e c2d c3e c4e c5e

        #1 c1e s1e, s2d, s3e Selected
        #2 c2d s1e, s2d, s3e Not Selected
        #3 c3e s2d, s4d, s5d Not Selected
        #4 c4e Not Selected
        #5 c5e s2d, s3e, s4d Selected
    """
    def setUp(self):
        self.category1 = Category.objects.create(name = "Category1", is_active = True)
        self.category2 = Category.objects.create(name = "Category2", is_active = False)
        self.category3 = Category.objects.create(name = "Category3", is_active = True)
        self.category4 = Category.objects.create(name = "Category4", is_active = True)
        self.category5 = Category.objects.create(name = "Category5", is_active = True)

        self.service1 = Services.objects.create(name = "Service1")
        self.service101 = Services.objects.create(name = "Service101")
        self.category101 = Category.objects.create(name="Category101")
        self.service101.categories.add(self.category101)

        self.service1_for_category1 = Services.objects.create(name = "Service1", is_active = True)
        self.service2_for_category1 = Services.objects.create(name = "Service2", is_active = False)
        self.service3_for_category1 = Services.objects.create(name = "Service3", is_active = True)

        self.service1_for_category2 = Services.objects.create(name = "Service1", is_active = True)
        self.service2_for_category2 = Services.objects.create(name = "Service2", is_active = False)
        self.service3_for_category2 = Services.objects.create(name = "Service3", is_active = True)
        
        self.service1_for_category3 = Services.objects.create(name = "Service1", is_active = False)
        self.service2_for_category3 = Services.objects.create(name = "Service2", is_active = False)
        self.service4_for_category3 = Services.objects.create(name = "Service4", is_active = False)

        self.service1_for_category5 = Services.objects.create(name = "Service1", is_active = False)
        self.service2_for_category5 = Services.objects.create(name = "Service2", is_active = False)
        self.service3_for_category5 = Services.objects.create(name = "Service3", is_active = True)



        self.category1.services.add(self.service1_for_category1, self.service2_for_category1, self.service3_for_category1)
        self.category2.services.add(self.service1_for_category2, self.service2_for_category2, self.service3_for_category2)
        self.category3.services.add(self.service1_for_category3, self.service2_for_category3, self.service4_for_category3)
        self.category5.services.add(self.service1_for_category5, self.service2_for_category5, self.service3_for_category5)
        

    def test_create_category(self):
        print("Creating category...")
        category1 = Category.objects.create(name = "Category6")
        print("Category created !")

        # checking category name is equal to the name we entered
        self.assertEqual(category1.name, "Category6")
        print("Test 1 passed !")

        # checking created category exist in Category in db
        self.assertTrue(Category.objects.filter(name="Category6").exists())
        print("Test 2 passed !")

    def test_create_service(self):
        print("Creating Service..")
        service1 = Services.objects.create(name="Service10", description="This is service1")
        # direct assignment of category1 is prohibited using categoryies.set() instead
        service1.categories.set([self.category1])
        print("Service Created !")
        service1.categories
        # checking category created or not
        try:
            self.assertEqual(service1.name, "Service10")
            print("Test 3 passed !")
        except Exception as e:
            print(e)

        # checking service1 exists in Service
        try:
            self.assertTrue(Services.objects.filter(name="Service1").exists())
            print("Test 4 passed !")
        except Exception as e:
            print(e)

    def test_add_category_1_2_to_service1(self):

        print("Adding category1 and category2 to service1..")
        # add category1 and category2 in service1
        self.service1.categories.add(self.category1, self.category2)
        print("Added category1 and category2 to service1")

        # check if category1 and category2 exist in service1
        self.assertTrue(self.service1.categories.filter(name="Category1").exists())
        self.assertTrue(self.service1.categories.filter(name="Category2").exists())
        print("Test 5 passed !")

        # count for duplicate check 
        self.assertEqual(1,self.service1.categories.filter(name="Category1").count())
        self.assertEqual(1,self.service1.categories.filter(name="Category2").count())
        print("Test 6 passed !")

    def test_remove_category1_from_service1(self):

        # get Service1
        service1 = Services.objects.get(name="Service101")

        # get Category1 from Service1
        category_to_remove = service1.categories.get(name="Category101")

        # remove category1 from service1
        service1.categories.remove(category_to_remove)

        # self.service1.categories.remove(self.category1)

        # check if it's removed successfully !
        service_instance = Services.objects.get(name="Service101")
        self.assertFalse(service_instance.categories.filter(name="Category1").exists())
        print("Test 7 passed !")
    
    def test_add_category_2_3_to_service_with_categories_1_2(self):
        self.service1.categories.add(self.category2, self.category3)
        self.assertTrue(self.service1.categories.filter(name="Category2").exists())
        self.assertTrue(self.service1.categories.filter(name="Category3").exists())

    def test_remove_category_2_from_service1(self):
        self.service1.categories.remove(self.category2)
        self.assertFalse(self.service1.categories.filter(name="Category2").exists())
    
    def test_categories_with_is_active_false(self):
        if Category.objects.filter(is_active=False):
            print("Categories without staff status ", Category.objects.filter(is_active=False).count())
            self.assertTrue(Category.objects.filter(is_active=False))
        else:
            print("Is staff not found")
    
    def test_get_enable_categories_with_atleast_one_enabled_service(self):
        categories = get_enable_categories_with_atleast_one_enabled_service()
        self.assertIsNotNone(categories)
        category_count = categories.count()
        self.assertEquals(categories.count(), category_count)
        values = categories.values()

    def test_disassociate_category_from_service(self):
        category1 = Category.objects.create(name = "Category100")
        service1 = Services.objects.create(name = "Service100")
        service1.categories.add(category1)
        service_with_categories_before = service1.categories.all().count()
        disassociate_category_from_service(service1, category1)
        service_with_categories_after = service1.categories.all().count()
        self.assertNotEqual(service_with_categories_after, service_with_categories_before)

    def test_update_the_details_of_service(self):
        new_name = 'Updated Service Name'
        new_description = 'Updated Description'

        # Retrieve the service and update details
        service_to_update = Services.objects.get(name = "Service101")
        service_to_update.name = new_name
        service_to_update.description = new_description
        # Update other fields as needed

        # Save the changes
        service_to_update.save()

        # Retrieve the updated service from the database
        updated_service = Services.objects.get(id=self.service.id)

        # Check if the details have been updated
        self.assertEqual(updated_service.name, new_name)
        self.assertEqual(updated_service.description, new_description)
        

    def tearDown(self):
        Category.objects.all().delete()
        Services.objects.all().delete()

        


        