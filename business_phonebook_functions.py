# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:03:28 2019

@author: Katharina
"""
from phonebook_database import *

#---------------------------------------------#
#Filtering Business Table by Business Category
#---------------------------------------------#


##---creates list of all business categories---###
##SELECT DISTINCT SQLitetutorial possible as well ##
business_category_list = []
def create_business_category_list():
    c.execute('SELECT * FROM business_table')
    for row in c.fetchall():
        if row[7] not in business_category_list:
            business_category_list.append(row[7])
    return business_category_list
create_business_category_list()

###---Returns all information where business_category = user_category---###
def extract_business_type_list(user_category):
    c.execute('SELECT * FROM business_table WHERE business_category =?', (user_category,))
    for row in c.fetchall():
        print(row)
        
        
        
###---Generates list of postcodes for businesses from extract_business_type_list()---###     
business_category_postcode_list = []        
def extract_business_type_postcode_list(user_category):    
    c.execute('SELECT * FROM business_table WHERE business_category =?', (user_category,))    
    for row in c.fetchall():
        if row[4] not in business_category_postcode_list:
            business_category_postcode_list.append(row[4])
    print('see if we get the postcodes', business_category_postcode_list)
    return(business_category_postcode_list)




###---Getting latitude and longitude from user's postcode---###  
def getting_latlong_from_user():  
    user_location = input('What postcode would you like to search? ')
    postcode_response = requests.get(endpoint_postcode + user_location)
    data_postcode = postcode_response.json()
    
    if data_postcode['status'] == 200:
        longitude = data_postcode['result'] ['longitude']
        latitude = data_postcode['result'] ['latitude']
        latlong = [latitude, longitude]
        return latlong
    
    else:
        print('Postcode not recognized!')



###---Getting latitude and longitude from business_category_postcode_list---###  
def getting_latlong_from_business():
    c.execute('SELECT longitude, latitude FROM business_table INNER JOIN geopointe_table ON (business_table.postcode = geopointe_table.postcode) WHERE last_name ="Imorts"')
    for row in c.fetchall():
        print(row)
#join_tables()






###---user inputs which business type to filter results by---###        
def sort_business_type():
    user_category = input('Choose one of the following business types{}'.format(business_category_list))
    extract_business_type_list(user_category)
 
    extract_business_type_postcode_list(user_category)
    
    latlong = getting_latlong_from_user() 
    print('This is the latlong', latlong)


sort_business_type()



