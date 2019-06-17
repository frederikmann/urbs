import pandas as pd
import unittest
from urbs.identify import *
from urbs.input import read_input

class TestCase(unittest.TestCase):

    def test_thing_1_init(self):
        thing_id = 'ABC'
        thing1 = 'ABC'
        self.assertEqual(thing_id, thing1)


class TestIdentify(unittest.TestCase):

    def setUp(self):
        input = 'mimo-example.xlsx'
        
        self.data = read_input(input, 2016)
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
