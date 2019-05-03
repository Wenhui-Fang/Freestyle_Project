from uszipcode import SearchEngine
import PySimpleGUI as sg  
import pytest
import sys
import zipcodes

dashline = "____________________________________"

#Simpe GUI adapted from https://pypi.org/project/PySimpleGUI/, allowing the users to set their preferences
layout = [[sg.Text('Welcome to use Tell-Me-Where-To-Live', size=(30, 1), font=("Helvetica", 25), text_color='blue')],      
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

#Input validation using zipcodes package - Zipcode; terminates the application if wrong input is captured
try:
         zipcodes.matching(values['_zipcode_'])
except: 
        TypeError
        sg.Popup("Warning!","You must enter a right zip code. The application will terminate now. Please start again...")
        sys.exit()

#Input validation - Miles to commute;
if values[0] == True:
        miles_to_commute = 10
elif values[1] == True:
        miles_to_commute = 30
elif values[0] == True and values[0] == True:
        miles_to_commute = 30
else: 
        sg.Popup("Warning!","You must select miles you are willing to commute. The application will terminate now. Please start again...")
        sys.exit()

#Read the users' preferred housing;
if values[2] == True:
        housing_style = "studio"
elif values[3] == True:
        housing_style = "1b1b"

#Read the users' budget
if values[4] == "<= $1,000":
        budget = "less than $1,000."
elif values[4] == "> $1,000":
        budget = "more than $1,000."

#Input Validation complete, start using built-in functions within uszipcode package to search data
user_zipcode = values['_zipcode_']  
search = SearchEngine(simple_zipcode=False)
zipcode = search.by_zipcode(user_zipcode)

#converting data to dictionary
matching_zip = zipcode.to_dict()

#Some zip code are associated with PO Box which requires a different way of presenting location
if matching_zip["post_office_city"] != "None":
        matching_city = matching_zip["post_office_city"]
else:
        matching_city = (matching_zip["county"] + ", " + matching_zip['state'])

#Let the users know their input with a pop-up window
sg.Popup('Input Verification',"So you will be studying or working in " + matching_city + ". And you are willing to commute up to " + 
str(miles_to_commute) + " miles. You want a " + housing_style + " and your budget is " + budget + ". Click Ok to Proceed.")

#using built-in data within uszipcode package to determine latitude and longtitude of the target zipcode/location
latitude = matching_zip["lat"]
longtitude = matching_zip["lng"]

#using built-in functions within uszipcode package to search nearby neighborhodds, setting maximum 10 neighborhoods for now
nearby_neighborhoods = search.by_coordinates(latitude, longtitude, radius=int(miles_to_commute),returns=10)

where_to_live = []
housing_listing = []
print("Below is a list of neighborhoods you can consider: \n")

#searching 5
for i in range(0,6):
    city = nearby_neighborhoods[i].post_office_city
    if city not in where_to_live:
        where_to_live.append(city)
        if housing_style == "studio":
                housing_listing = nearby_neighborhoods[i].monthly_rent_including_utilities_studio_apt
        elif housing_style == "1b1b":
                housing_listing = nearby_neighborhoods[i].monthly_rent_including_utilities_1_b
        print(city + "\n")

# print housing listing

print("Monthly rent including utilities for a " + housing_style + " is as follows: \n")
print("Price Range: " + "       " + "Number of listings: ")
print(dashline)
number_of_listing = len(housing_listing)

for i in range(0, 6):
    print((housing_listing[0]["values"][i]["x"]).ljust(10) + ":"+ (str(housing_listing[0]["values"][i]["y"]).rjust(25)))

# breakpoint()

# sg.Popup("Below is a list of neighborhoods you can consider:", where_to_live)

# print=sg.Print  
# for i in range(0, 6):
#         sg.Print((housing_listing[0]["values"][i]["x"]).ljust(10) + ":"+ (str(housing_listing[0]["values"][i]["y"]).rjust(25)))

# #to hold above print list
# sg.PopupScrolled(print("Price Range: " + "       " + "Number of listings: "))
