# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:03:28 2019

@author: Katharina
"""
from phonebook_database import *

business_category_list = []

def create_business_category_list():
    c.execute('SELECT * FROM business_table')
    for row in c.fetchall():
        if row[7] not in business_category_list:
            business_category_list.append(row[7])
    return business_category_list
create_business_category_list()


def extract_business_type_list(user_category):
    c.execute('SELECT * FROM business_table WHERE business_category =?', (user_category,))
    for row in c.fetchall():
        print(row)
    return(row)
        
    

def sort_business_type():
    user_category = input('Choose one of the following business types{}'.format(business_category_list))

    extract_business_type_list(user_category)
        
sort_business_type()



