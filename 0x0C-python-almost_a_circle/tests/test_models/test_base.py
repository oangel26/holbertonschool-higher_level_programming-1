import unittest

""" test base module """
from models.base import Base
class TestBase(unittest.TestCase):
    ''' test base cases'''
    def test_base(self):
        ''' create with correct id'''
        base = Base(None)
        self.assertEqual(base.id, 1)
