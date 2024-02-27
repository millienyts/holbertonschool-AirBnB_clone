#!/usr/bin/python3
'''
    test_city.py
    
    Unittest for class City
'''
import unittest
from models.city import City
from datetime import datetime

class TestCity(unittest.TestCase):
    '''
        Class City Unittest
    '''

    def setUp(self):
        '''
            Setup before each test method
        '''
        self.city_instance = City()
        self.city_instance.name = "San Francisco"
        self.city_instance.state_id = "CA"

    def test_initial_attributes(self):
        '''
            Test initial attribute values
        '''
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertIsInstance(city.id, str)

    def test_attributes(self):
        '''
            Test setting City instance attributes
        '''
        self.assertEqual(self.city_instance.name, "San Francisco")
        self.assertEqual(self.city_instance.state_id, "CA")

    def test_save_method(self):
        '''
            Test save method updates `updated_at` attribute
        '''
        old_updated_at = self.city_instance.updated_at
        self.city_instance.save()
        self.assertNotEqual(self.city_instance.updated_at, old_updated_at)

    def test_to_dict_method(self):
        '''
            Test to_dict method includes correct keys
        '''
        city_dict = self.city_instance.to_dict()
        self.assertIn("id", city_dict)
        self.assertIn("name", city_dict)
        self.assertIn("state_id", city_dict)
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)
        self.assertEqual(city_dict['__class__'], 'City')

if __name__ == "__main__":
    unittest.main()
