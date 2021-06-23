import unittest

""" unittest base module """
from models.base import Base


class TestBase(unittest.TestCase):
    ''' test base cases'''

    def setUp(self):
        self.base = Base(None)

    def tearDown(self) -> None:
        self.base = None
        Base.reset()


    def test_creation(self):
        ''' validate type and instance'''
        self.assertEqual(type(self.base), Base)
        self.assertEqual(isinstance(self.base, Base), True)


    def test_base_id(self):
        ''' create with correct id'''
        self.assertEqual(self.base.id, 1)

    def test_increment_id(self):
        ''' increment id'''
        self.assertEqual(self.base.id, 1)
        self.base = Base(None)

        self.assertEqual(self.base.id, 2)

        self.base = Base(12)
        self.assertEqual(self.base.id, 12)

        self.base = Base(0)
        self.assertEqual(self.base.id, 0)

        self.base = Base(22)
        self.assertEqual(self.base.id, 22)

        self.base = Base('base')
        self.assertEqual(self.base.id, 'base')
