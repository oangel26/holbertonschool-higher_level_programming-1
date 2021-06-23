import unittest

""" test base module """
from models.base import Base


class TestBase(unittest.TestCase):
    ''' test base cases'''

    def setUp(self):
        Base.reset()

    def test_1_0(self):
        """Create new instances: check for id."""

        b0 = Base()
        self.assertEqual(b0.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
