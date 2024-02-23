#!/usr/bin/python3
import unittest
from models.city import City
from datetime import datetime

class TestCity(unittest.TestCase):
    """Tests for the City class."""
    def setUp(self):
        """Set up test methods."""
        self.city_instance = City()
        self.city_instance.name = "San Francisco"
        self.city_instance.state_id = "CA"

    def test_attributes(self):
        """Test the attributes of City instances."""
        self.assertEqual(self.city_instance.name, "San Francisco")
        self.assertEqual(self.city_instance.state_id, "CA")
        self.assertIsInstance(self.city_instance.id, str)
        self.assertIsInstance(self.city_instance.created_at, datetime)
        self.assertIsInstance(self.city_instance.updated_at, datetime)

if __name__ == "__main__":
    unittest.main()
