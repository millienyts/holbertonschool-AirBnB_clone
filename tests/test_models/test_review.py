#!/usr/bin/python3
import unittest
from models.review import Review
from datetime import datetime

class TestReview(unittest.TestCase):
    """Tests for the Review class."""
    def setUp(self):
        """Set up test methods."""
        self.review_instance = Review()
        self.review_instance.place_id = "1001"
        self.review_instance.user_id = "1001"
        self.review_instance.text = "Great place!"

    def test_attributes(self):
        """Test the attributes of Review instances."""
        self.assertEqual(self.review_instance.place_id, "1001")
        self.assertEqual(self.review_instance.user_id, "1001")
        self.assertEqual(self.review_instance.text, "Great place!")
        self.assertIsInstance(self.review_instance.id, str)
        self.assertIsInstance(self.review_instance.created_at, datetime)
        self.assertIsInstance(self.review_instance.updated_at, datetime)

if __name__ == "__main__":
    unittest.main()

'''
    test_review.py
    
    Unittest for class Review
'''
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    '''
        Class Review unittest
    '''

    def test_review_attributes(self):
        '''
            Class Review test cases
        '''
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
