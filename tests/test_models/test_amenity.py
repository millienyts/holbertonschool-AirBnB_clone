#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from datetime import datetime

class TestAmenity(unittest.TestCase):
    """Tests for the Amenity class."""
    def setUp(self):
        """Set up test methods."""
        self.amenity_instance = Amenity()
        self.amenity_instance.name = "Wi-Fi"

    def test_attributes(self):
        """Test the attributes of Amenity instances."""
        self.assertEqual(self.amenity_instance.name, "Wi-Fi")
        self.assertIsInstance(self.amenity_instance.id, str)
        self.assertIsInstance(self.amenity_instance.created_at, datetime)
        self.assertIsInstance(self.amenity_instance.updated_at, datetime)

if __name__ == "__main__":
    unittest.main()
