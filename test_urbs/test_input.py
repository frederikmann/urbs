import unittest
from datetime import date
from urbs.input import read_input

class TestInput(unittest.TestCase):

    def setUp(self):
        input = 'test_urbs/Input/minTest.xlsx'
        year = date.today().year
        self.data = read_input(input, year)

    def test_inputframe_isempty(self):
        print(self.data)



