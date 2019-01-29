# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 14:03:48 2019

@author: winkl
"""

import unittest
from business_phonebook_functions import *

#NB: must has "test" in function name
class testFunctions(unittest.TestCase):
    def test_if_no_connection_db(self):
        self.assertTrue(getdb())
        
    def test_check_returns_business_list(self):
        self.assertIsInstance(create_business_category_list(),list)
#checking returned list not empty, if empty will return False
        self.assertTrue(create_business_category_list())
        
    def test_extract_business_type_list(self, user_category):
        self.assertIsInstance()

        
if __name__ == "__main__":
    unittest.main()