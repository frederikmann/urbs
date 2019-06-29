import unittest
from datetime import date
from urbs.identify import identify_mode
from urbs.input import read_input


class TestIdentify(unittest.TestCase):

    def setUp(self):
        input = 'mimo-example.xlsx'
        year = date.today().year
        self.data = read_input(input, year)
        #print("read input")
        #print("identifing mode")
        self.mode = identify_mode(self.data)
        #print(self.mode)
        

    def test_identify_mode(self):
        #print("testing mode")        
        self.assertEqual(self.mode, {'int': False, 
                                    'tra': True, 
                                    'sto': True, 
                                    'dsm': True, 
                                    'bsp': True, 
                                    'tve': True, 
                                    'exp': {'pro': True, 'tra': True, 'sto-c': True, 'sto-p': True}
                                    })
        #print("tested mode")
