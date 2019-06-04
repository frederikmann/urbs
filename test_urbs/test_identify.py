import pandas as pd
import unittest
from urbs.identify import *

class TestCase(unittest.TestCase):

    def test_thing_1_init(self):
        thing_id = 'ABC'
        thing1 = 'ABC'
        self.assertEqual(thing_id, thing1)

'''
class TestIdentify(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame.from_dict({
            'field_1': [1, 2],
            'field_2': [3, 4]
            })

    def test_identify_mode(self):
        mode = identify_mode(self.data)
        self.assertEqual(mode, 0)
 '''