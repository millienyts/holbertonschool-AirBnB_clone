#!/usr/bin/python3
import unittest
from models.place import Place
from datetime import datetime

class TestPlace(unittest.TestCase):
    """Tests for the Place class."""
    def setUp(self):
        """Set up test methods."""
        self.place_instance = Place()
        self.place_instance.name = "My lovely house"
        self.place_instance.city_id = "0001"
        self.place_instance.user_id = "0001"
        self.place_instance.number_rooms = 4
        self.place_instance.number_bathrooms = 2
        self.place_instance.max_guest = 2
        self.place_instance.price_by_night = 100
        self.place_instance.latitude = 120.0
        self.place_instance.longitude = 90.0
        self.place_instance.amenity_ids = []

    def test_attributes(self):
        """Test the attributes of Place instances."""
        self.assertEqual(self.place_instance.name, "My lovely house")
        self.assertEqual(self.place_instance.city_id, "0001")
        self.assertEqual(self.place_instance.user_id, "0001")
        self.assertEqual(self.place_instance.number_rooms, 4)
        self.assertEqual(self.place_instance.number_bathrooms, 2)
        self.assertEqual(self.place_instance.max_guest, 2)
        self.assertEqual(self.place_instance.price_by_night, 100)
        self.assertEqual(self.place_instance.latitude, 120.0)
        self.assertEqual(self.place_instance.longitude, 90.0)
        self.assertEqual(self.place_instance.amenity_ids, [])
        self.assertIsInstance(self.place_instance.id, str)
        self.assertIsInstance(self.place_instance.created_at, datetime)
        self.assertIsInstance(self.place_instance.updated_at, datetime)

if __name__ == "__main__":
    unittest.main()
