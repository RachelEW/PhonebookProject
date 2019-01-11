# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 10:08:31 2019

@author: winkl
"""

import json
import sqlite3 #importing SQLite toolkit

#with open('mock_data_business.json') as json_file:  
#    data = json.load(json_file)
##    print(data)
#    for line in data:
#        print(line, "\n\n")
#        print(line["business name"])

with open('mock_data_business.json') as json_file:  
    business_data = json.load(json_file)
#    print(data)
    business_name_list = []
    for i in business_data:
        business_info = phonebook2
#        print(line, "\n\n")
#        print(line["business name"])
        bName = line["business name"]
        bNameStr = str(bName)
        print(bNameStr)
        business_name_list.extend(bNameStr)
        print(business_name_list)

with open('mock_data_people.json') as json_file2:
    people_phonebook = json.load(json_file2)
    first_names = []
    for i in range(len(phonebook)):
       person_info = phonebook[i]
       first_name = person_info ['first_name']
       first_names.append(first_name)
    print(first_names)      
        
    
#
#conn = sqlite3.connect('test1.db') #as we are creating te database we can just name the database fie with .db at the end
#c = conn.cursor() #conenct to cursor, low level pointer specifically used in databases to find positions of data in each data table
#
#def create_table_business():
#    c.execute("CREATE TABLE IF NOT EXISTS BusinessPhonebook(business_name TEXT , address_line_1 TEXT, address_line_2 TEXT, address_line_3 TEXT, postcode TEXT, country TEXT, telephone_number REAL, business_type TEXT)")
#    
##NB: 'CREATE TABLE IF NOT EXISTS' is the command to create and check the existance of a table
#
#def data_entry():
#    c.execute("INSERT INTO BusinessPhonebook(12233222, '2018-01-1', 'python', 5)")
#    conn.commit() #running commit command after inserting values into a database
#    c.close()
#    conn.close()
#    
#def dynamic_data_entry():
#    unix = time.time()
#    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
#    keyword = 'Python'
#    value = random.randrange(0, 10)
#    c.execute('INSERT INTO stuffToBuild(unix, datestamp, keyword,value)VALUES (?, ?, ?, ?)', (unix, date, keyword,value))
#    conn.commit()