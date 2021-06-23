import unittest

""" test base module """
from models.base import Base


class TestBase(unittest.TestCase):
    ''' test base cases'''

    def setUp(self):
        self.base = Base(None)

    def tearDown(self) -> None:
        self.base = None
        Base.reset()

    def test_base_id(self):
        ''' create with correct id'''
        self.assertEqual(self.base.id, 1)

    def test_increment_id(self):
        ''' increment id'''
        self.assertEqual(self.base.id, 1)
        self.base = Base(None)
        self.assertEqual(self.base.id, 2)
