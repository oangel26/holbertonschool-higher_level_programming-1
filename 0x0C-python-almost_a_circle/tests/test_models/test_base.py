import unittest

""" test base module """
from models.base import Base


class TestBase(unittest.TestCase):
    ''' test base cases'''

    def setUp(self):
        self.base = Base(None)

    def tearDown(self) -> None:
        Base.reset()

    def test_base_id(self):
        ''' create with correct id'''
        base = Base(None)
        self.assertEqual(base.id, 1)
