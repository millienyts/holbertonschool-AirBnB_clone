#!/usr/bin/python3
"""Unittests for State class."""
import unittest
from models.state import State

class TestState(unittest.TestCase):
    """Test the State class."""

    def test_attributes(self):
        """Test State attributes."""
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")
