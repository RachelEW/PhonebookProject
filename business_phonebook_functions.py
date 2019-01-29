# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:03:28 2019

@author: Katharina
"""
from phonebook_database import *
from math import radians, sin, asin, cos, atan, atan2, sqrt

#---------------------------------------------#
#Connect to database
#---------------------------------------------#

def getdb():
    try:
        conn = sqlite3.connect('phonebook2.db')
        c = conn.cursor()
        return c
    except:
        return False

#---------------------------------------------#
#Filtering Business Table by Business Category
#---------------------------------------------#


##---creates list of all business categories---###
##SELECT DISTINCT SQLitetutorial possible as well ##

def create_business_category_list():
    try:
        c = getdb()
        c.execute('SELECT distinct (business_category) FROM business_table')
        results = c.fetchall()
        new_results = [i[0] for i in results]  
    #    print(new_results)      
        return new_results
    except:
        return False
#create_business_category_list()

###---Returns all information where business_category = user_category---###
def extract_business_type_list(user_category):
    c = getdb()
    c.execute('SELECT * FROM business_table WHERE business_category =?', (user_category,))
    business_results = [row for row in c.fetchall()]
#    for row in c.fetchall():
#        business_results.append(row)
    return business_results
        
        
        
###---Generates list of postcodes for businesses from extract_business_type_list()---###     
business_category_postcode_list = []        
def extract_business_type_postcode_list(user_category):
    business_results = extract_business_type_list(user_category)    
#    c.execute('SELECT * FROM business_table WHERE business_category =?', (user_category,))    
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

#---Getting latitude and longitude from business_category_postcode_list---###
def getting_latlong_from_business(user_category):
    c.execute('SELECT latitude, longitude from business_table INNER JOIN geopointe_table ON (business_table.postcode = geopointe_table.postcode) WHERE business_category =?', (user_category, ))
    results = c.fetchall()
    return results
    

###---Calculating distance between user's postcode and postcodes in database---###
distance_list = []
def calculate_haversine_distance(latlong, results):
    lat2 = radians(latlong[0])
    lon2 = radians(latlong[1])
    print(lat2,lon2)
    for item in results:
       lat1 = radians((item[0]))
       lon1 = radians((item[1]))
       print('This is lat1',lat1)
       print('This is lon1',lon1)
       dlon = lon2 - lon1
       print('This is dlon: ',dlon)
       dlat = lat2 - lat1
       print('This is dlat: ',dlat)
       a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
       print('This is a: ',a)
       c = 2 * atan2( sqrt(a), sqrt(1-a))
       print('This is c: ',c)
       d = 6371 * c
       print('This is the distance in km: ',d)
       distance_list.append(d)
    return distance_list



###---user inputs which business type to filter results by---###        
def sort_business_type():
    user_category = input('Choose one of the following business types{}'.format(business_category_list))
    extract_business_type_list(user_category)
 
    extract_business_type_postcode_list(user_category)
    
    latlong = getting_latlong_from_user() 
    print('This is the latlong', latlong)
    results = getting_latlong_from_business(user_category)
    distance = calculate_haversine_distance(latlong, results)
    print('This is the list of distances', distance)

#sort_business_type()



