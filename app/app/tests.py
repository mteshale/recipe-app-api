"""
Sample tests
"""

from app import calc

from django.test import SimpleTestCase


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_substruct_numbers(self):
        """Test substructing numbers"""
        res = calc.substruct(10, 15)

        self.assertEqual(res, 5)
