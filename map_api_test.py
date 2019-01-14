# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 09:18:27 2019

@author: winkl
"""

import sqlite3
import requests
#import phonebook2

###---connecting to database---###

###---creating a database and cursor---###
conn = sqlite3.connect('phonebook2.db')
c = conn.cursor()

###---looking up Postcodes from person table---###

postcode_list = []

def read_postcode_person_phonebook():
    c.execute('SELECT * FROM people_table ')
    for row in c.fetchall():
        postcode_list.append(row[5])
        print(postcode_list)

#def find_postcode():
#    for i in range(len(postcodes_list)):
        
        
#main_url = "https://api.postcodes.io/postcodes/"
#endpoint = "https://api.postcodes.io/postcodes/"
#payload = {"q": "London,UK", "units":"metric", "appid":"API KEY"}
#
#response = requests.get(endpoint, params=payload)
#data = response.json() #in a json format
#
#print('This is what data looks like\n')
#print(data)
#
#print (response.url)
#print(response.status_code)
#print(response.headers["content-type"])
        
read_postcode_person_phonebook()