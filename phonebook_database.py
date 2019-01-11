# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 13:40:33 2019

@author: winkl
"""

import sqlite3
import json

###---creating a database and cursor---###
conn = sqlite3.connect('phonebook2.db')
c = conn.cursor()

###################
"""People Table"""
###################

###---import random names from json file---###
with open('mock_data_people2.js') as people_phonebook:
 phonebook1 = json.load(people_phonebook)
# print(phonebook1)
 
###---Creating a table within the database with column names---###
def create_table_people():
   c.execute('CREATE TABLE IF NOT EXISTS people_table(first_name TEXT , last_name TEXT, address_line_1 TEXT, address_line_2 TEXT, address_line_3 TEXT, postcode TEXT, country TEXT, telephone_number REAL)')
#create_table_people()

###---Adding data from json file of random people to table in database (for loop to loop through values)---###
def data_entry_people():
   for i in range(len(phonebook1)):
       person_info = phonebook1[i]
       first_name = person_info ['first_name']
       last_name = person_info ['last_name']
       address_line_1 = person_info ['address_line_1']
       address_line_2 = person_info ['address_line_2']
       address_line_3 = person_info ['address_line_3']
       country = person_info ['country']
       postcode = person_info ['postcode']
       telephone_number = person_info ['telephone_number']
#       print(first_name, last_name, address_line_1, address_line_2, address_line_3, postcode, country, telephone_number)
       c.execute('INSERT INTO people_table(first_name, last_name, address_line_1, address_line_2, address_line_3, postcode, country, telephone_number) VALUES (?, ?, ?, ? , ? , ? , ?, ?)', (first_name, last_name, address_line_1, address_line_2, address_line_3, postcode, country, telephone_number))
       conn.commit()
#   c.close()
#   conn.close()
#data_entry_people()

###---Retrieving row from table which has "Simmonds" as the value for the column "last_name"---###
def read_from_people_phonebook1():
    c.execute('SELECT * FROM people_table WHERE last_name ="Simmonds" ')
    for row in c.fetchall():
        print(row)
        
#####################
"""Business Table"""
#####################

###---import random business names from json file---###
with open('mock_data_business2.js') as business_phonebook:
 phonebook2 = json.load(business_phonebook)
# print(phonebook2)
 
###---Creating a table within the database with column names---###
def create_table_business():
   c.execute('CREATE TABLE IF NOT EXISTS business_table(business_name TEXT , address_line_1 TEXT, address_line_2 TEXT, address_line_3 TEXT, postcode TEXT, country TEXT, telephone_number REAL, business_category TEXT)')
#create_table_business()

###---Adding data from json file of random businesses to table in database (for loop to loop through values)---###
def data_entry_business():
   for i in range(len(phonebook2)):
       business_info = phonebook2[i]
       business_name = business_info ['business name']
       address_line_1 = business_info ['address_line_1']
       address_line_2 = business_info ['address_line_2']
       address_line_3 = business_info ['address_line_3']
       country = business_info ['country']
       postcode = business_info ['postcode']
       telephone_number = business_info ['telephone_number']
       business_category = business_info ['business_category']
#       print(business_name, address_line_1, address_line_2, address_line_3, postcode, country, telephone_number, business_category)
       c.execute('INSERT INTO business_table(business_name, address_line_1, address_line_2, address_line_3, postcode, country, telephone_number, business_category) VALUES (?, ?, ?, ? , ? , ? , ?, ?)', (business_name, address_line_1, address_line_2, address_line_3, postcode, country, telephone_number, business_category))
       conn.commit()
   c.close()
   conn.close()
#data_entry_business()
   
###---Retrieving row from table which has "Home" as the value for the column "business_category"---###
def read_from_business_phonebook_1():
    c.execute('SELECT * FROM business_table WHERE business_category ="Home" ')
    for row in c.fetchall():
        print(row)

################
"""TESTING"""
################

#read_from_people_phonebook1()
read_from_business_phonebook_1()
        