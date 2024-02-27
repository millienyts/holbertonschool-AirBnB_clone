#!/usr/bin/python3
'''
    test_place.py
    
    Unittest for Class Place
'''
import unittest
from models.place import Place
from datetime import datetime

class TestPlace(unittest.TestCase):
    '''
        Class Place unittest
    '''

    def setUp(self):
        """Set up test methods."""
        self.place = Place()
        self.place.name = "My lovely house"
        self.place.city_id = "0001"
        self.place.user_id = "0001"
        self.place.number_rooms = 4
        self.place.number_bathrooms = 2
        self.place.max_guest = 2
        self.place.price_by_night = 100
        self.place.latitude = 120.0
        self.place.longitude = 90.0
        self.place.amenity_ids = []

    def test_place_attrs(self):
        '''
            Class Place test cases
        '''
        self.assertEqual(self.place.city_id, "0001")
        self.assertEqual(self.place.user_id, "0001")
        self.assertEqual(self.place.name, "My lovely house")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 4)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.max_guest, 2)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 120.0)
        self.assertEqual(self.place.longitude, 90.0)
        self.assertEqual(self.place.amenity_ids, [])
        self.assertIsInstance(self.place.id, str)
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)

if __name__ == '__main__':
    unittest.main()
