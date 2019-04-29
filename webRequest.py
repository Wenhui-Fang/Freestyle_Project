import requests
import xml.etree.ElementTree as ET
# import xmltodict
from bs4 import BeautifulSoup
from uszipcode import SearchEngine
import re
import PySimpleGUI as sg  

dashline = "____________________________________"

#Simpe GUI adapted from https://pypi.org/project/PySimpleGUI/
layout = [[sg.Text('Welcome to use the App', size=(30, 1), font=("Helvetica", 25), text_color='blue')],      
   [sg.Text('Please enter the zip code where you will work or go to college')],      
   [sg.Text('zipcode', size=(15, 1)), sg.InputText('20057', key='_zipcode_')],
   [sg.Text('Please determine how many miles you are willing to commute, and your desired room plan.',)],       
   [sg.Checkbox('< 10 miles', size=(10,1)),  sg.Checkbox('10 - 30 miles', default=True)],
   [sg.Radio('I want a studio!     ', "RADIO1", default=True, size=(10,1)), sg.Radio('I want 1b1b!', "RADIO1")],      
[sg.Text('My Monthly Budget is:', size=(18, 1))],    
[sg.InputCombo(['<= $1,000', '> $1,000'], size=(20, 3))],      
[sg.Submit(), sg.Cancel()]]    
event, values  = sg.Window('OPIM 242 FreeStyle Project', auto_size_text=True, default_element_size=(40, 1)).Layout(layout).Read()    

# print(values)
# {'_zipcode_': '20057', 0: True, 1: True, 2: True, 3: False, 4: '<= $1,000'}

if values[0]:
        miles_to_commute = 10
else:
        miles_to_commute = 30

user_zipcode = values['_zipcode_']  

if values[2]:
        housing_style = "studio"
elif values[3]:
        housing_style = "1b1b"

if values[4] == "<= $1,000":
        budget = "less than $1,000."
else:
        budget = "more than $1,000."
# sg.Popup(event, "Are you sure??") 

# user_zipcode = input("Please tell me where you will work / go to college by entering the zip code...")

#using uszipcode package to request data
search = SearchEngine(simple_zipcode=False)
zipcode = search.by_zipcode(user_zipcode)

#converting data to dictionary
matching_zip = zipcode.to_dict()
matching_city = matching_zip["post_office_city"]
matching_state = matching_zip["state"]

sg.Popup('Input Verification',"So you will be studying or working in " + matching_city + ". And you are willing to commute up to " + str(miles_to_commute) + " miles. Click Ok to Proceed")

# print("So you will be studying or working in " + matching_city + ".")

latitude = matching_zip["lat"]
longtitude = matching_zip["lng"]

miles_to_commute = 30

# nearby_neighborhoods = search.by_coordinates(latitude, longtitude, radius=int(miles_to_commute), returns=5)
nearby_neighborhoods = search.by_coordinates(latitude, longtitude, radius=int(miles_to_commute),returns=10)

where_to_live = []
housing_listing = []
print("Below is a list of neighborhoods you can consider: \n")

for i in range(0,5):
    city = nearby_neighborhoods[i].post_office_city
    if city not in where_to_live:
        where_to_live.append(city)
        if housing_style == "studio":
                housing_listing = nearby_neighborhoods[i].monthly_rent_including_utilities_studio_apt
        elif housing_style == "1b1b":
                housing_listing = nearby_neighborhoods[i].monthly_rent_including_utilities_1_b
        print(city + "\n")

# print(housing_listing)

print("Monthly rent including utilities for a " + housing_style + "is as follows: \n")
print("Price Range: " + "       " + "Number of listings: ")
print(dashline)
number_of_listing = len(housing_listing)

for i in range(0, 6):
    print((housing_listing[0]["values"][i]["x"]).ljust(10) + ":"+ (str(housing_listing[0]["values"][i]["y"]).rjust(25)))

# breakpoint()